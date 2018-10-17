import getpass
import os.path
import sys
import string


def load_data(filepath):
    with open(filepath, 'rb') as file:
        return file.read()


def get_password_char_strength(password):
    strength_lower = 0
    strength_upper = 0
    strength_digit = 0
    strength_specials = 0
    for char in password:
        if char.islower():
            strength_lower = 1
        if char.isupper():
            strength_upper = 2
        if char.isdigit():
            strength_digit = 2
        if string.punctuation.find(char) > -1:
            strength_specials = 4
    return strength_upper + strength_digit + strength_lower + strength_specials


def get_password_strength(password, password_blacklist):
    min_password_length = 4
    if password_blacklist.count(password) > 0:
        return '1 (the password in blacklist)'
    elif len(password) < min_password_length:
        return '1 (the password less than 4 symbols)'
    else:
        strength_len = 1
        return strength_len + get_password_char_strength(password)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('need filename')
    user_filepath = sys.argv[1]
    if not os.path.exists(user_filepath):
        exit('need correct file path')
    user_password = getpass.getpass(prompt='Password: ', stream=None)
    password_blacklist = load_data(user_filepath)
    print('Your password strength is:{}'
          .format(get_password_strength(user_password, password_blacklist)))
