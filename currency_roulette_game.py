
# pip install currencyconverter

import random
from currency_converter import CurrencyConverter

print()

def get_money_interval(amount, difficulty):
    cc = CurrencyConverter()
    amount_in_ils = cc.convert(amount, 'USD', 'ILS')
    print(amount_in_ils)
    return amount_in_ils-(10-difficulty), amount_in_ils+(10-difficulty)


def get_guess_from_user(amount):
    user_input = input(f"Guess how much in ILS is {amount} USD: ")
    if not user_input.isnumeric():
        print("Invalid number")
        return get_guess_from_user(amount)

    return float(user_input)


def compare_results(guess, amount, difficulty):
    (range_from, range_to) = get_money_interval(amount, difficulty)
    return range_from <= guess <= range_to


def get_random_amount():
    rnd = random.Random()
    return rnd.randrange(1, 101)


def play(difficulty):
    amount = get_random_amount()
    guess = get_guess_from_user(amount)
    return compare_results(guess, amount, difficulty)
