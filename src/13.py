import random

def get_random_number(minimum=0, maximum=100):
    return random.randint(minimum, maximum)

def get_random_string(length=8):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(letters) for i in range(length))

def get_random_color():
    colors = ["red", "green", "blue", "yellow", "purple"]
    return random.choice(colors)
