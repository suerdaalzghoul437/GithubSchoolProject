import random

def get_random_code():
    numbers = "1234567890"
    letters = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%^&*()-=+[]{};:,./<>?"
    code = ""
    for i in range(10):
        code += random.choice(numbers)
        code += random.choice(letters)
        code += random.choice(symbols)
    return code