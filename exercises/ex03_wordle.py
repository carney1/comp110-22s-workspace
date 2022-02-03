
__author__: str = "730337797"


def input_guess(expected_length: int) -> str:
    """Check for valid input"""
    user_guess = input("Enter a 5 character word: ")
    while len(user_guess) != expected_length:
        user_guess = input("That wasn't 5 chars! Try again: ")
    return user_guess

    
def contains_char(guessed_word: str, single_character: str) -> bool:
    """determine if letter in given word"""
    assert len(single_character) == 1
    j: int = 1
    letter_match: bool = False
    while len(guessed_word) >= j:
        if single_character == guessed_word[len(guessed_word) - j]:
            return True
            letter_match = True
        j = j + 1
    if letter_match is False:
        return False


def emojified(guessed_word: str, secret_word: str):
    """Finds how closely guessed word matches secret word"""
    assert len(guessed_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    p: str = ""
    while i < len(guessed_word):
        if guessed_word[i] == secret_word[i]:
            p = p + GREEN_BOX
        else:
            letter_match: bool = contains_char(secret_word, guessed_word[i])
            if letter_match:
                p = p + YELLOW_BOX   
            else:
                p = p + WHITE_BOX
        i = i + 1
    return p
        

def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret_word: str = "codes"
    k: int = 1
    correct_answer: bool = False
    while k <= 6:
        print(f"=== Turn {k}/6 ===")
        expected_length = 5
        user_guess: str = input_guess(expected_length)
        p: str = emojified(user_guess, secret_word)
        print(p)
        if user_guess == secret_word:
            print(f"You won in {k}/6 turns!")
            k: int = 6
            correct_answer = True
        k = k + 1
    if correct_answer is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()