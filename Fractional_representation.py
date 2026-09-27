x = float(input("Enter your fraction: "))

# This code bloack is to find the power of 2 to make the number and integer
p = 0
while ((2 ** p)*x)%1 != 0:
    print("Remainder: " + str((2 ** p) * x - int((2 ** p)* x)))
    p += 1

# THis gives the bumber that converts the fraction into whole number
num = int(x * (2 ** p))

#conversion of that number into binary
result = ""
if num == 0:
    result = "0"
while num > 0:
    result = str(num % 2) + result
    num = num // 2

# Right shift 
for i in range( p - len(result)):
    result = '0' + result

# Adding Decimal
result = result[0 : -p] + '.' + result[-p:]

# final result 
print(f"The binary representation of {str(x)} is {result}")