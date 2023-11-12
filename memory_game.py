import random
import time


def generate_sequence(difficulty):
    rnd = random.Random()
    lst = []
    for i in range(difficulty):
        lst.append(rnd.randrange(1, 101))
    return lst


def get_list_from_user(difficulty):
    lst = []
    user_input = input("Enter the numbers (separated by commas): ")
    input_list = user_input.split(',')
    if len(input_list) != difficulty:
        print(f"List must have {difficulty} elements")
        return get_list_from_user(difficulty)
    for i in range(difficulty):
        input_element = input_list[i].strip()
        if not input_element.isnumeric():
            print(f"element {input_element} is not a number")
            return get_list_from_user(difficulty)
        lst.append(int(input_element))
    return lst


def is_list_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


def print_and_prepare_for_hide(arg, sleep_in_seconds):
    print(arg, end='')
    time.sleep(sleep_in_seconds)
    print('\r', end='')


def play(difficulty):
    lst_numbers = generate_sequence(difficulty)
    print_and_prepare_for_hide(lst_numbers, 0.7)
    lst_guess = get_list_from_user(difficulty)
    return is_list_equal(lst_numbers, lst_guess)
