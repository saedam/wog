import memory_game
import guess_game
import currency_roulette_game
from score import add_score

def welcome():
    person_name = input()
    print(f"Hi {person_name} and welcome to the World of Games: The Epic Journey")


def start_play():

    game_num = 0
    while game_num == 0:
        print(
"""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
2. Guess Game - guess a number and see if you chose like the computer.")
3. Currency Roulette - try and guess the value of a random amount of USD in ILS"""
        )

        user_input = input()
        if not (user_input.isnumeric() and 1 <= int(user_input) <= 3):
            print("bad choice")
        else:
            game_num = int(user_input)
            break

    difficulty = 0

    while difficulty == 0:
        print("Please choose a difficulty level between 1 and 5")
        user_input = input()
        if not (user_input.isnumeric() and 1 <= int(user_input) <= 5):
            print("bad choice")
        else:
            difficulty = int(user_input)
            break


    result = False
    match game_num:
        case 1:
            result = memory_game.play(difficulty)
        case 2:
            result = guess_game.play(difficulty)
        case 3:
            result = currency_roulette_game.play(difficulty)

    if result is True:
        print("You Won")
        add_score(difficulty)
    else:
        print("You Lost")



