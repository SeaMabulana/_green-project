import re


def validate_password(password):
    while True:
        if len(password) < 8:
            return 'Make sure your password is at lest 8 letters'
        elif re.search('[0-9]', password) is None:
            return 'Make sure your password has a number in it'
        elif re.search('[A-Z]', password) is None:
            return 'Make sure your password has a capital letter in it'
        elif re.search('[^a-zA-Z0-9]', password) is None:
            return 'Make sure your password has a special character in it'
        else:
            return True

# function that creates usersname using first alphabet of f-name and l-name with 6 digits
def create_username(first_name, last_name, model):
    import random
    unique_username = str(
        f'{first_name.lower()[0]}{last_name.lower()[0]}{random.randrange(000000, 999999)}'
    )
    while model.objects.filter(username=unique_username).exists():
        unique_username += str(
            f'{first_name.lower()[0]}{last_name.lower()[0]}{random.randrange(000000, 999999)}'
        )
    else:
        _username = unique_username
    return _username
