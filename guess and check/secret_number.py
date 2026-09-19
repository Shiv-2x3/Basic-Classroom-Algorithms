secret_number = 5

found = False

for num in range(1 , 11):
    if num == secret_number:
        print("Found" ,num)
        found = True
if not found:
    print("Not Found")