import random


def generate_number(difficulty):
    rnd = random.Random()
    return rnd.randrange(0, difficulty + 1)


def get_guess_from_user(difficulty):
    user_input = input(f"Enter a number between 0 and {difficulty}: ")
    if not user_input.isnumeric():
        print("Invalid number")
        return get_guess_from_user(difficulty)
    entered_number = int(user_input)
    if not (0 <= entered_number <= difficulty):
        print("Number out of range")
        return get_guess_from_user(difficulty)

    return entered_number


def compare_results(number_guess, secret_number):
    return number_guess == secret_number


def play(difficulty):
    secret_number = generate_number(difficulty)
    number_guess = get_guess_from_user(difficulty)
    return compare_results(number_guess, secret_number)

