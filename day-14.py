from resources.day14.game_data import data
from resources.day14.art import logo, vs
from random import choice
import os


def compare_followers(a, b):
    if a['follower_count'] > b['follower_count'] or a == b:
        return 'A', a
    else:
        return 'B', b


def game_start():

    game_over = False
    score = 0
    a_person = choice(data)
    b_person = choice(data)

    print(logo)

    while not game_over:

        print(f"Compare A: {a_person['name']}, a {a_person['description']} from {a_person['country']}.")
        print(vs)
        print(f"Against B: {b_person['name']}, a {b_person['description']} from {b_person['country']}.")

        answer, a_person = compare_followers(a_person, b_person)
        guess = input("Who has more followers? ").upper()

        if answer == guess:
            score += 1
            b_person = choice(data)
            os.system('cls') # Clears terminal for Windows user
            print(logo)
            print(f"Your current score is: {score}")

        else:
            os.system('cls')
            print(f"Sorry, that's wrong. Final Score: {score}")
            game_over = True


game_start()
