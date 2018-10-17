# Password Strength Calculator

The script checked input password strength according Wikipedia advices [https://en.wikipedia.org/wiki/Password_policy](https://en.wikipedia.org/wiki/Password_policy). Strength calculated as integer from 1 to 10. File with passwords blacklist took here [https://github.com/danielmiessler/SecLists/blob/master/Passwords/UserPassCombo-Jay.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/UserPassCombo-Jay.txt)

# Quickstart

Run **password_strength.py** with  path to text file of passwords blacklist as parameter. 

Example of script launch on Linux, Python 3.5:

```bash

$ python password_strength.py <filepath>

Password:

Your passwords strength:10
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
