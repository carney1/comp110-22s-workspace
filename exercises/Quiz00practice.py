low: int = 1
high: int = 100

guess: int = (low + high) // 2
print(guess)

response: str = input("is guess higher, lower, or correct?")

while response == "higher":
    low = guess - 1
    print(guess)
    response: str = input("is guess too high, too low, or correct?")
while response == "lower":
    high = guess - 1
    print(guess)
    response: str = input("is guess too high, too low, or correct?")
while response == "correct":
    print("Correct!")
