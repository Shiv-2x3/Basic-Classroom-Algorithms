an_letter ='aefhilmnorsxAEFHILMNORSX'

word = input("I will cheer for you! Enter a word: ")
times = int(input('Enthusiasm level (1 - 10)'))

for c in word:
    if c in an_letter:
        print(f'give me an {c}: {c}')
    else:
        print(f'Give me a {c}: {c}')
print("What's that spell? ")
for i in range(times):
    print(word , "!!!")