This folder contains pyinstaller compiled binaries for Debian 10 (Buster) and Windows 10 (1909).
The following AntiVirus software *falsely* identifies the Windows binary as a trojan/malware:


Antiy-AVL - Trojan[PSW]/Python.Agent

SecureAge APEX - Malicious

Cybereason - Malicious.289e17

Cynet - Malicious (score: 100)

Gridinsoft - Trojan.Win64.Agent.oa!s1

Jiangmin - Trojan.PSW.Python.at

Microsoft (Windows Defender et. al.) - Trojan:Win32/Glupteba!ml

Tencent - Malware.Win32.Gencirc.11ba19a2

Yandex - Trojan.RegRun!hO0NykKcr0w

Zillya - Tool.Convagent.Win32.58

So you'll need to set an exclusion in those AVs in order to use it unmolested under Windows.
Otherwise, just install Python for windows and run the script natively.


***SHA265 Hashes***

Debian Binary (telnet-enable2) - 5b9eb9abe05669bbff54c2c5d7d8fb310912be66b7ed3a7ceb6f523ce8ad1d3a

Windows Binary (telnet-enable2.exe) - ab2f5566f252d3391a2332b050e258e8afa7e736d54930199ecd0332358d7489
