s = input("Enter your word: ")
count = 0
seen = "" 
for char in s:
    if char not in seen:
        seen += char
        count += 1
print(f"This are the unique letters {count}")