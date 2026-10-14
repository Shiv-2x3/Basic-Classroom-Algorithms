def Bisection_search(x):
    """
    Checks for Bisection search square root
    """
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
    return print(f"The square root is close to {guess}")

#Test Cases
Bisection_search(4)
Bisection_search(25)
Bisection_search(9)

print("===============")

for x in range(5):
    Bisection_search(x)
