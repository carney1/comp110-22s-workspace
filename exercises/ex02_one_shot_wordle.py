"""Exercise 2 Comp 110!"""
__author__: str = "730337797"

secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")

while len(secret_word) != len(user_guess):
    user_guess = input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
j: int = 1
p: str = ""

while i < len(secret_word):
    if user_guess[i] == secret_word[i]:
        p = p + GREEN_BOX   
    else:
        j = 1
        letter_match: bool = False
        while len(secret_word) >= j:
            if user_guess[i] == secret_word[len(secret_word) - j]:
                p = p + YELLOW_BOX
                letter_match = True
            j = j + 1
        if letter_match is False:
            p = p + WHITE_BOX
    i = i + 1
print(p)


if secret_word == user_guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
