from resources.day4ascii import rock, paper, scissors
from random import choice


def play_again():
    play_again = input("Play again? Type yes or no: ").lower()
    if play_again == 'no':
        return False
    else:
        return True


choices = [rock, paper, scissors]

player_score = 0
com_score = 0

play_game = True

while play_game:

    com_choice = choice(choices)

    try:
        player_choice = int(input("Let's play! Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS:\n"))

        if player_choice in (0, 1, 2):
            print("You chose:")
            print(choices[player_choice])

            print("Opponent chose: ")
            print(com_choice)

            if player_choice == choices.index(com_choice):
                print("Draw")
                print(f"SCORE: Player -> {player_score} | Opponent -> {com_score}")
                play_game = play_again()

            elif ((player_choice == 0 and choices.index(com_choice) == 2)
                  or (player_choice == 1 and choices.index(com_choice) == 0)
                  or (player_choice == 2 and choices.index(com_choice) == 1)):
                print("You win.")
                player_score += 1
                print(f"SCORE: Player -> {player_score} | Opponent -> {com_score}")
                play_game = play_again()

            else:
                print("You lost.")
                com_score += 1
                print(f"SCORE: Player -> {player_score} | Opponent -> {com_score}")
                play_game = play_again()

        else:
            print("You've entered an invalid response.")

    except ValueError:
        print("You've entered an invalid response.")
