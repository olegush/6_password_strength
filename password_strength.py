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
    msgs = {
        'in_black': 'The password in blacklist.',
        'didnt_check_black': 'But its did not check with blacklist.',
        'less_than_4': 'The password less than 4 symbols.'
    }
    safety = 1
    msg = ''
    if passwords_blacklist:
        if password in passwords_blacklist:
            safety = 0
            msg = msgs['in_black']
    else:
        msg = msgs['didnt_check_black']
    min_password_length = 4
    if len(password) < min_password_length:
        safety = 0
        msg = msgs['less_than_4']
    strength = safety * get_password_char_strength(password)
    return msgs, strength, msg


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            user_filepath = sys.argv[1]
            passwords_blacklist = load_data(user_filepath).splitlines()
        else:
            passwords_blacklist = None
        user_password = getpass.getpass(prompt='Password: ', stream=None)
        msgs, strength, msg = get_password_strength(user_password,
                                                    passwords_blacklist)
        print ('Error codes:')
        for code, err in msgs.items():
            print(err)
        print('\nYour password strength: {} {}'.format(strength, msg))
    except IOError:
        print ('No such file or directory')
