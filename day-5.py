import string
import random

letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

password = []

running = True

while running:

    try:
        num_letters = int(input("How many letters in your password? "))
        num_digits = int(input("How many digits in your password? "))
        num_symbols = int(input("How many punctuations in your password? "))

        for _ in range(0, num_letters):
            password.append(random.choice(letters))

        for _ in range(0, num_digits):
            password.append(random.choice(digits))

        for _ in range(0, num_symbols):
            password.append(random.choice(symbols))

        running = False

    except ValueError:
        print("Please write a valid number. Let's try that again.")

random.shuffle(password)
str_password = ''.join(password)

print(f"Your new password is: {str_password}")