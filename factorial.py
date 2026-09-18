number = int(input("Enter your Number: "))
loop = input("enter the loop you want to use: ")

n = 1
factorial = 1
if loop == "while":
    while n  <= number:
        factorial = factorial * n
        n = n + 1
    print("While loop: ")
    print(f"Factorial of the {number} is {factorial}")

elif loop == "for":
    for i in range(1 , number+1 , 1):
        factorial *= i
    print("For loop: ")
    print(f"Factorial of the {number} is {factorial}")