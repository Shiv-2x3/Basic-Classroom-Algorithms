prompt = input("Input your Word: ")
counter = 0
for i in range(len(prompt)):
    if prompt[i] == prompt[-i+1]:
        counter += 1
print(f'count of similar letters are {counter}')

