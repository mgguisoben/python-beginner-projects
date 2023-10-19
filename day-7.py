from resources.day7.hangman_art import logo, stages
from resources.day7.hangman_words import word_list
import random

word = list(random.choice(word_list))
guesses = len(stages)
correct_guesses = ['_' for _ in range(len(word))]
already_guessed = []

print(logo)
print(f"The word has {len(word)} letters.")

guessed = False

while not guessed:

    if word == correct_guesses:
        print("You guessed it!")
        guessed = True

    else:

        print(f"{' '.join(correct_guesses)}")

        guess = input("Guess a letter: ").lower()

        if guess in already_guessed:
            print("You've already guessed that letter")

        elif guess in word:
            already_guessed.append(guess)
            for index, letter in enumerate(word):
                if guess == letter:
                    correct_guesses[index] = guess

        else:
            already_guessed.append(guess)

            if guesses == 1:
                print(stages[0])
                print("You just died.")
                guessed = True

            else:
                print(stages[guesses - 1])

            guesses -= 1
