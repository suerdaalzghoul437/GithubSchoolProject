import random

def generate_random_code(n):
    """Generate a string of n uppercase letters and numbers"""
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(chars) for _ in range(n))
