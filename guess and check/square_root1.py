guess = 0
x = int(input("Enter your number: "))
while guess ** 2 < x:
    guess += 1
    if guess ** 2  == x:
        print(f"This is a perfect square: {x}")
    else:
        print(f'{x} is not a perfect square')