import string


def caesar_cipher(shift, letters):
    cipher_letters = []

    for x in range(shift - 1, 26):
        cipher_letters.append(letters[x])
    for y in range(0, shift - 1):
        cipher_letters.append(letters[y])

    return cipher_letters


def encode(shift, word, letters):
    cipher_letters = caesar_cipher(shift, letters)
    cipher_digits = []
    secret_word = ''

    for letter in word:
        cipher_digits.append(letters.index(letter))
    for digit in cipher_digits:
        secret_word += cipher_letters[digit]

    return secret_word


def decode(shift, word, letters):
    cipher_letters = caesar_cipher(shift, letters)
    cipher_digits = []
    secret_word = ''

    for letter in word:
        cipher_digits.append(cipher_letters.index(letter))
    for digit in cipher_digits:
        secret_word += letters[digit]

    return secret_word


letters = list(string.ascii_lowercase)

running = True
while running:
    method = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()

    if method == 'encode':
        word = input("Type your message: \n")
        shift = int(input("Type the shift number: \n")) % 26
        secret_word = encode(shift, word, letters)
        print(f"Here's the encoded message: {secret_word}")

    elif method == 'decode':
        word = input("Type your message: \n")
        shift = int(input("Type the shift number: \n")) % 26
        secret_word = decode(shift, word, letters)
        print(f"Here's the decoded message: {secret_word}")

    else:
        print("You've typed an invalid response.")

    go_again = input("Type 'yes' if you want to go again. Otherwise, 'no':\n")
    if go_again == 'no':
        running = False
