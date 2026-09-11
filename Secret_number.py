secret_number = 3 
user_input = int(input("Enter the number bet 1 - 10: "))
if secret_number == user_input:
    print("Booyah!! You gussed it")
elif user_input > secret_number:
    print("This is big")
else:
    print("This is small")