print("== Binary Conversion ==")
x = int(input("Enter the number: "))


if x < 0:
    is_neg = True
    x = abs(x)
else:
  is_neg = False
Binary = ""  
while x > 0:
    Binary = str(x % 2) + Binary
    x = x//2

if is_neg:
   Binary = '-' + Binary
print(f'The binary conversion of {x} is {Binary}')