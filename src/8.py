import random

def get_random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "for i in range(5):\n\tprint(i)"
    elif num == 3:
        return "numbers = [1, 2, 3, 4, 5]\nfor n in numbers:\n\tprint(n)"
    elif num == 4:
        return "x = input('Enter a number: ')\ny = int(x)\nprint(y + 1)"
    else:
        return "def get_random_python_code():\n\treturn ''.join(chr(random.randint(0, 25)) for _ in range(1000))"