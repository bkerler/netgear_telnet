# Netgear Enable Telnet (New Crypto) for Netgear Orbi LBR20 (possibly works for others in the Orbi famlily and beyond)
(c) B.Kerler 2021-2022
Licensed under MIT License

## Installation
- Python 3 >=3.8 needed

## Usage :

```bash
./telnet-enable2.py <ip> <mac> <username> ['<password>']
```
Ex:
```
./telnet-enable2.py 192.168.1.1 A0:40:A0:69:B6:30 admin 'mypassword'
```

- ip is usually 192.168.1.1
- mac is mac of br0 interface (In the Orbi web setup: Advanced / Advanced Home / Router Information / MAC Address)
- username is usually "admin"
- password is your unhashed Web GUI password. Use quotes if password 
  includes ampersand or parenthesis

## Confirmed to Work on:

- Orbi LBR20
- Orbi RBR40 (v2.7.3.22)
- Nighthawk AX12 / RAX120v2 V1.2.8.40
- Nighthawk RAX75 V1.0.1.58_1.0.24, V1.0.10.140_1.0.79
 
## Prepared but untested:
- Orbi RBR760 (V6.3.1.0)
- Orbi NBR750 (V1.5.43+r49254)
- Orbi RBR850 (V4.6.9.11_2.3.5)
- Orbi RBRE960 (V6.0.3.85)

## Credits :
- https://github.com/jashandeep-sohi/python-blowfish (Sorry, I had to mod your blowfish)

- Paul Gebheim's original code from 2009, which no longer works

- hazarjast, who pushed me to do it and spent me a pizza :D
