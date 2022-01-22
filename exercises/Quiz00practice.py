"""Quiz 00 Prep"""
x: int = int(input("Type X Value Here "))
y: int = int(input("Type Y Value Here "))
if x > y:
    x = x + y
    z = x + y // 2
else:
    if x == y:
        x = x - y
        z = x + y // 2
    else:
        x = x ** y
        z = x + y // 2
print(z)

username: str = input("Insert Name ")
print("Hello There, " + username + ", Have a Good Day!")