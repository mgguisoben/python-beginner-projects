from resources.day7.art import logo, stages
from resources.day7.words import word_list
import random
import os
import time

word = list(random.choice(word_list))
guesses = len(stages)
correct_guesses = ['_' for _ in range(len(word))]
already_guessed = []

guessed = False

while not guessed:

    print(logo)
    print(f"The word has {len(word)} letters.")
    print(stages[6])

    if word == correct_guesses:
        print("You guessed it!")
        guessed = True

    else:

        print(f"{' '.join(correct_guesses)}")

        guess = input("Guess a letter: ").lower()

        if guess in already_guessed:
            print("You've already guessed that letter")
            time.sleep(2)
            os.system('cls')

        elif guess in word:
            already_guessed.append(guess)
            for index, letter in enumerate(word):
                if guess == letter:
                    correct_guesses[index] = guess
            os.system('cls')

        else:
            already_guessed.append(guess)

            if guesses == 1:
                guessed = True

            else:
                print(stages[guesses - 1])
            guesses -= 1
        os.system('cls')

print(stages[6])
print("You just died.")