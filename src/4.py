def get_random_code():
    import random
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*"
    password = ""
    for i in range(10):
        password += random.choice(letters)
        password += random.choice(numbers)
        password += random.choice(symbols)
    return password
