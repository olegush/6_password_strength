import getpass
import sys
import string


def load_data(filepath):
    with open(filepath, 'r') as file:
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
            strength_upper = 3
        if char.isdigit():
            strength_digit = 2
        if char in string.punctuation:
            strength_specials = 4
    return strength_upper + strength_digit + strength_lower + strength_specials


def get_password_strength(password, passwords_blacklist):
    msgs = [
        'The password in blacklist.',
        'But its did not check with blacklist.',
        'The password less than 4 symbols.'
    ]
    safety = 1
    msg = ''
    if passwords_blacklist:
        if password in passwords_blacklist:
            safety = 0
            msg = msgs[0]
    else:
        msg = msgs[1]
    min_password_length = 4
    if len(password) < min_password_length:
        safety = 0
        msg = msgs[2]
    strength = safety * get_password_char_strength(password)
    return strength, msg


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            user_filepath = sys.argv[1]
            passwords_blacklist = load_data(user_filepath).splitlines()
        else:
            passwords_blacklist = None
    except IOError:
        print('No such file or directory')
    else:
        user_password = getpass.getpass(prompt='Password: ', stream=None)
        strength, msg = get_password_strength(user_password,
                                              passwords_blacklist)
        print('Your password strength: {} {}'.format(strength, msg))
