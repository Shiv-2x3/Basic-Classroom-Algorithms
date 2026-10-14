x = int(input("Number to find the square root of: "))

epsilion = 0.01

num_guessed = 0

low = 0

high = x

guess = (high + low) / 2.0

while (guess ** 2 - x) >= epsilion:
    if guess ** 2 < x:
        low = guess

    else:
        high = guess

    guess = (high + low) / 2.0
    num_guessed += 1

print(f"Num We guessed is {num_guessed}")
print(f"The square root is {guess}")

