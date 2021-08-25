# Netgear Enable Telnet (New Crypto) for Netgear Orbi LBR20 (possibly works for others in the Orbi famlily and beyond)
(c) B.Kerler 2021
Licensed under MIT License

## Installation
- Python 3 >=3.8 needed

## Usage :

```bash
./telnet-enable2.py <ip> <mac> <username> [<password>]
```
Ex:
```
./telnet-enable2.py 192.168.1.1 A0:40:A0:69:B6:30 admin <yourpass>
```
- ip is usually 192.168.1.1
- mac is mac of br0 interface
- username is usually "admin"
- password is your unhashed Web GUI password


## Credits :
- https://github.com/jashandeep-sohi/python-blowfish (Sorry, I had to mod your blowfish)

- Paul Gebheim's original code from 2009, which no longer works

- hazarjast, who pushed me to do it and spent me a pizza :D
