import random

def generate_random_number():
    """Returns a random number between 1 and 100."""
    return random.randint(1, 100)

if __name__ == "__main__":
    print("Random number:", generate_random_number())
