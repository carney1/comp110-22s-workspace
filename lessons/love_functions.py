"""Some examples of loving function definitions"""

def love(name: str) -> str:
    """Given a name as a paremeter, returns a loving string."""
    return f"I love you {name}!"

print(love("Holly"))

def spread_love(to: str, n: int) -> str:
    """Generates a string that repeate a loving message n times."""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note += love(to) + "\n"
        counter += 1
    return love_note

# print function in REPL for line break to occur

def mystery(n: int) -> str:
    """A useless function."""
    i: int = 0
    while i < n:
        if i % 2 == 1:
            return "ooh"  #as soon as evaluation of function reaches a return statement, function call is done
        i += 1
    return "ahh"