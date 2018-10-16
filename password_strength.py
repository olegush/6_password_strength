def get_password_char_strength(password):
    strength_lower = 0
    strength_upper = 0
    strength_digit = 0
    strength_specials = 0
    for char in list(password):
        if char.islower():
            strength_lower = 1
        if char.isupper():
            strength_upper = 2
        if char.isdigit():
            strength_digit = 2
        if '!@#$%^&*()_+|<>?~`'.find(char) > -1:
            strength_specials = 4
    return strength_upper + strength_digit + strength_lower + strength_specials


def get_password_strength(password, password_blacklist):
    if password_blacklist.count(password) > 0:
        return 1
    elif len(password) < 4:
        return 1
    else:
        strength_len = 1
        return strength_len + get_password_char_strength(password)


if __name__ == '__main__':
    user_password = raw_input('Password:')
    password_blacklist = ['Password1',
                          'Welcome1',
                          'P @ ssword',
                          'Summer1!',
                          'password',
                          'Fa$hion1',
                          'Hello123',
                          'Welcome123',
                          'P @ ssword1']
    print('Your password\'s strength:{}'
          .format(get_password_strength(user_password, password_blacklist)))
