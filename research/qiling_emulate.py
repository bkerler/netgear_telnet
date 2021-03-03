#!/usr/bin/env python3
# Netgear telnetenable emulator via Qiling
# (c) B.Kerler 2021, licenced under MIT

import sys, os

sys.path.append("..")
from qiling import *
from unicorn import *
from unicorn.arm_const import *
import logging
from Library.utils import *
from struct import pack, unpack
import time

password=b"test"
mac=bytes.fromhex("000102030405")

def replace_function(ql, addr, callback):
    def runcode(ql):
        ret = callback(ql)
        ql.reg.r0 = ret
        ql.reg.pc = ql.reg.lr

    ql.hook_address(runcode, addr)


def hook_mem_read(uc, access, address, size, value, user_data):
    if address > 0xF000000:
        pc = uc.reg_read(UC_ARM_REG_PC)
        print("READ of 0x%x at 0x%X, data size = %u" % (address, pc, size))


def hook_code(uc, access, address, size):
    pc = uc.reg_read(UC_ARM_REG_PC)
    #if 0x11A40< pc < 0x11BF4:
    #    print("PC at 0x%x" % (pc))
    if pc==0x11B74:
        length = uc.reg_read(UC_ARM_REG_R2)
        r1 = uc.reg_read(UC_ARM_REG_R1)
        w = uc.mem_read(r1, length)
        print("Strcat: " + hexlify(w).decode('utf-8'))
    if pc==0x11B80:
        length = uc.reg_read(UC_ARM_REG_R2)
        r1 = uc.reg_read(UC_ARM_REG_R1)
        w = uc.mem_read(r1, length)
        print("Data to MD5: " + hexlify(w).decode('utf-8'))
    if pc==0x11BB8:
        length=uc.reg_read(UC_ARM_REG_R2)
        r0=uc.reg_read(UC_ARM_REG_R0)
        r1=uc.reg_read(UC_ARM_REG_R1)
        v=uc.mem_read(r0,length)
        w=uc.mem_read(r1,length)
        print("Blowfish Key Length: " + hex(length))
        print("Blowfish Key: "+w.decode('utf-8'))
    elif pc==0x11BCC:
        length = uc.reg_read(UC_ARM_REG_R3)
        r0 = uc.reg_read(UC_ARM_REG_R0)
        r1 = uc.reg_read(UC_ARM_REG_R1)
        r2=0xc221000
        uc.reg_write(UC_ARM_REG_R2,0xc221000)
        v = uc.mem_read(r0, length)
        w = uc.mem_read(r1, length)
        print("Blowfish Payload: " + hexlify(w).decode('utf-8'))
    elif pc == 0x11BD4:
        r2 = 0xc221000
        w = uc.mem_read(r2, 0xB0)
        print("Blowfish Data: " + hexlify(w).decode('utf-8'))
        uc.emu_stop()

def hook_mem_invalid(uc, access, address, size, value, user_data):
    pc = uc.reg_read(UC_ARM_REG_PC)
    if access == UC_MEM_WRITE:
        info = ("invalid WRITE of 0x%x at 0x%X, data size = %u, data value = 0x%x" % (address, pc, size, value))
    if access == UC_MEM_READ:
        info = ("invalid READ of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_FETCH:
        info = ("UC_MEM_FETCH of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_READ_UNMAPPED:
        info = ("UC_MEM_READ_UNMAPPED of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_WRITE_UNMAPPED:
        info = ("UC_MEM_WRITE_UNMAPPED of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_FETCH_UNMAPPED:
        info = ("UC_MEM_FETCH_UNMAPPED of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_WRITE_PROT:
        info = ("UC_MEM_WRITE_PROT of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_FETCH_PROT:
        info = ("UC_MEM_FETCH_PROT of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_FETCH_PROT:
        info = ("UC_MEM_FETCH_PROT of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    if access == UC_MEM_READ_AFTER:
        info = ("UC_MEM_READ_AFTER of 0x%x at 0x%X, data size = %u" % (address, pc, size))
    print(info)
    return False


def main():
    filename = "telnetenable"
    data = open(filename, "rb").read()
    elfheader = elf(data, filename)
    pt = patchtools()

    ql = Qiling([filename], rootfs=".", output="default")
    ql.gdb = "0.0.0.0:9999"
    ql.arch.enable_vfp()

    def config_match(ql):
        return 0

    def config_get(ql):
        ql.reg.R0 = 0xc221000
        ql.mem.write(0xc221000, password)
        return ql.reg.R0

    def ioctl(ql):
        ql.mem.write(ql.reg.R2+18, mac)
        return 0

    def socket(ql):
        return 1

    def close(ql):
        return 0

    def memset(ql):
        dst = ql.reg.R0
        val = ql.reg.R1
        count = ql.reg.R2
        data = bytearray()
        for i in range(count):
            data.append(val)
        ql.mem.write(dst, bytes(data))
        return 0

    def strncpy(ql):
        data = ql.mem.read(ql.reg.R1, ql.reg.R2)
        rdata = bytearray()
        for d in data:
            if d == 0:
                break
            rdata.append(d)
        target = ql.reg.R0
        ql.mem.write(target, bytes(rdata))
        return len(rdata)

    def memmove(ql):
        data=ql.mem.read(ql.reg.R1,ql.reg.R2)
        print("Memmove: "+hexlify(data).decode('utf-8'))
        ql.mem.write(ql.reg.R0,bytes(data))
        return ql.reg.R2

    def snprintf(ql):
        dst=ql.reg.R0
        maxlen=ql.reg.R1
        fmt = bytearray()
        tmp = -1
        pos = 0
        while tmp != 0:
            v = ql.mem.read(ql.reg.R2 + pos,1)[0]
            if v == 0:
                break
            pos += 1
            fmt.append(v)

        value=bytearray()
        tmp = -1
        pos = 0
        while tmp != 0:
            v = ql.mem.read(ql.reg.R3 + pos,1)[0]
            if v == 0:
                break
            pos += 1
            value.append(v)

        data=fmt.decode('utf-8') % value[:maxlen].decode('utf-8')
        print(data)
        ql.mem.write(dst, bytes(data,'utf-8'))
        return len(data)

    def strcpy(ql):
        rdata = bytearray()
        tmp = -1
        pos = 0
        while tmp != 0:
            v = ql.mem.read(ql.reg.R1 + pos,1)[0]
            if v == 0:
                break
            pos += 1
            rdata.append(v)
        ql.mem.write(ql.reg.R0,bytes(rdata))
        return len(rdata)

    ql.uc.hook_add(UC_HOOK_MEM_INVALID, hook_mem_invalid)
    ql.uc.hook_add(UC_HOOK_MEM_READ, hook_mem_read)
    ql.uc.hook_add(UC_HOOK_CODE, hook_code)
    replace_function(ql, 0x10784, config_match)
    replace_function(ql, 0x107B4, config_get)
    replace_function(ql, 0x10700, socket)
    replace_function(ql, 0x106AC, ioctl)
    replace_function(ql, 0x10748, strncpy)
    replace_function(ql, 0x107C0, close)
    replace_function(ql, 0x10778, memset)
    replace_function(ql, 0x106C4, memmove)
    replace_function(ql, 0x106A0, strcpy)
    replace_function(ql, 0x106D0, snprintf)

    ql.reg.sp = 0x10774 + 0x12000  # SP from main

    ql.mem.map(0x13000, 0xD000)
    ql.mem.map(0x20000, 0x2000)
    ql.mem.map(0xc221000, 1024)
    ql.run(begin=0x11A40, end=0x11BF0)


if __name__ == "__main__":
    main()
