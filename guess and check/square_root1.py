guess = 0
flag = True
num =  int(input("Enter Number: "))
while guess ** 2 < num and flag:
    guess += 1
    if num < 0:
        flag = False
if guess ** 2 == num:
    print(f'{guess} is the perfect square for {num} ')
else:
    if num < 0:
        print("you accidently end up with a negative number.")
    else:
        print("opps !! this is not a perfect square..")