# Bisection Search for Secret Number 

print("== Bisection Search ==") 

print("-- Deciding Range --")


user_guess = int(input("Enter Your guess Between 0 - 10: ")) # Takes user input within range

correct_num = 3    #--> We have initialize for the secter number

Flag = True #  --> Set the flag so that we can terminate the loop whenever we want 


while Flag:

    # Condition 1 --> to check whether the number we guesses is equal or not
    if user_guess == correct_num:
        print("--Correct Guess--")
        Flag = False # --> This terminates the loop 

    # Condition 2 --> guess is high or low
    elif user_guess > correct_num:
        print("-- Too Big --") 
        user_guess = int(input(f"Enter your guess between 0 - {user_guess}: "))
        if user_guess == correct_num:
            print("-- Correct Guess --")
            Flag = False

    # Condition 3 --> guess is high or low
    elif user_guess < correct_num:
        print("-- Too Small --")
        user_guess = int(input(f'Enter your number between {user_guess} - 10: '))
        if user_guess == correct_num:
            print("-- Correct Guess --")
            Flag = False


print("-- End --")