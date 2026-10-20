lists =[1 , 2 , 3 , ["a" , "b" , "c"]]
lists_of_int = [1 , 2 ,3, 4 ,5,6,7,8,9]

#working with lists
empty_list = [] 

lenght_of_list = len(lists)
print(lenght_of_list)

list_index_to_1 = lists[1]
print(list_index_to_1)

list_idex_for_another_lists = lists[3][0]
print(list_idex_for_another_lists)

addition_of_lists = ['pikachu' , ' Charizad' , 'bulbasaur'] + [1 ,2 ,3 ,4 ,5]
print(addition_of_lists)

maximum_between_lists = max(lists_of_int)
print(maximum_between_lists)

list_indexing = lists[1 : 3]
print(list_indexing)

#looping over lists
for e in lists:
    print(e)

#lists mutation
lists[1] = "o"
print(lists[1])

# String to lists
vowels = "AEIOU"
print(list(vowels))

full_name = "shiv Dinesh Salunke"
print(full_name.split(" "))

# List to string
list_for_string = ["s" , "h" ,"i","v"]
A = "".join(list_for_string)
print(A)

# count words
def count_words(sen):
    words = sen.split(" ")
    return len(words)

print(count_words("Hello world how are you"))

#sort method
list_x = [1 , 3 , 5 , 2 , 9 , 7 , 6]
list_x.sort()


#reverse method 
list_x.reverse()

sorted_list = sorted(list_x)

def square_list(L):
    for i in range(len(L)):
        L[i] ==L[i] ** 2

L = [2 , 3 ,4 ]
square_list(L)
print(L)

print(id(L))
print(id(L.append(3))
print(id(L))
L.clear()
print(id(L))