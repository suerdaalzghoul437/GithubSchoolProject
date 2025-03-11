import random

def get_random_code(length=16):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(length):
        code += random.choice(letters)
    return code