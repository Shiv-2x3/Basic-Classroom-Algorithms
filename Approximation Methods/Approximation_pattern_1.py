x = 36

epsilion = 0.01

num_guess = 0

increment = 0.0001

guess = 0.0

while abs((guess **2 ) - x) >= epsilion:
    guess += increment
    num_guess += 1

print(f"num_guess {num_guess}")

print(f"The closest square root of {x} is {guess}")