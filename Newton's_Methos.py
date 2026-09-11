'''
1 . Finds root of the polynomial (f(g , x) = g ** 3 - x = 0)
2. Algorithm uses successive approximation 
next_guess = guess - f(guess) / f`(guess)

'''

x = int(input("What x to find the cube root of: "))
y = int(input("Start your guess with: "))

print(f"current estimate cubed: {y ** 3}")

next_guess = y - (((y ** 3) - x ) / 3 * y ** 2)
print(f'Next guess to try {int(next_guess)}')


