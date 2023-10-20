from random import randint


def check_guess(num, guess):
    if guess == num:
        print(f"You've guessed it. The number is {num}.")
        return True
    elif guess > num:
        print("Too HIGH.")
        return False
    elif guess < num:
        print("Too LOW.")
        return False


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


def game_start():
    print("Welcome to the number guessing game.")
    print("I'm thinking of a number between 1 and 100.")

    random_number = randint(1, 100)
    guesses = set_difficulty()
    guessed = False

    while not guessed:

        print(f"You have {guesses} attempts remaining to guess the number: ")
        player_guess = int(input("Make a guess: "))
        guessed = check_guess(player_guess, random_number)
        guesses -= 1

        if guesses == 0:
            print("You've run out of guesses, you lose.")
            return

        print("Guess again.")


game_start()
