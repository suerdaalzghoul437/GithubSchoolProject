import random

def play_random_game():
    # Example of a simple game that involves picking a random number between 1 and 10
    random_number = random.randint(1, 10)
    print(f"The computer picked a number: {random_number}")
    if random_number == 5:
        return "You win!"
    else:
        return f"Sorry, the correct number was {random_number}."

print(play_random_game())
