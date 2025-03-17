import random

def get_random_code(n=10):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_chars = '!@#$%^&*()-=+[{]}:;'

    code = ''
    for _ in range(n):
        code += random.choice(letters)
        code += random.choice(numbers)
        code += random.choice(special_chars)

    return code
