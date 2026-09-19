cube = int(input("Enter The number: "))

for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != cube:
    print("This is not an perfect cube")
else:
    if cube < 0:
        guess = -guess
        print(f'cube root of {str(cube) is {str(guess)}}')