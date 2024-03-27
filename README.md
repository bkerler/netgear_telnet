# Netgear Enable Telnet (New Crypto) for Netgear
(c) B.Kerler 2021-2024
Licensed under MIT License

## Installation
- Python 3 >=3.8 needed

## Usage :

```bash
./telnet-enable.py <ip> <mac> <username> ['<password>']
```
Ex:
```
./telnet-enable.py 192.168.1.1 A0:40:A0:69:B6:30 admin 'mypassword'
```

- ip is usually 192.168.1.1
- mac is mac of br0 interface (In the Orbi web setup: Advanced / Advanced Home / Router Information / MAC Address)
- username is usually "admin"
- password is your unhashed Web GUI password. Use quotes if password 
  includes ampersand or parenthesis

## Confirmed to Work on:

- Orbi LBR20
- Orbi 960 series v6.3.7.10
- Orbi RBR40 v2.7.3.22
- Orbi RBRE960 v6.0.3.85 - v6.3.7.5
- AX1800 / RAX10 V1.0.14.134
- Nighthawk AX7 / RAX70 V1.0.10.110
- Nighthawk AX6 / RAX50 V1.0.12.120_2.0.83
- Nighthawk AX12 / RAX120v2 V1.2.8.40 - V1.2.9.52
- Nighthawk RAX75 V1.0.1.58_1.0.24, V1.0.10.140_1.0.79
- Orbi NBR750 V4.6.5.11_1.5.43+r49254 - V4.6.14.3+r49254
- Orbi RBR850 V4.6.9.11_2.3.5 - V4.6.14.3_2.3.12
- LAX20 1.1.6.34
- Orbi RBR760 (V6.3.1.0 - V6.3.6.2_1.2.66)

## Credits :
- https://github.com/jashandeep-sohi/python-blowfish (Sorry, I had to mod your blowfish)

- Paul Gebheim's original code from 2009, which no longer works

- hazarjast, who pushed me to do it and spent me a pizza :D
