# append --> adds element in the list at the end
# official working 
lists = [0 , 1 , 2 , 3 , 4 ,5]
lists.append(6)
print(lists)

#usecase for append
a = []
for element in range(11):
    a.append(element)
print(a)

# construction of append like fuction
def append_by_me(lists , elements):
    lists[len(lists):] = [elements]

num = []
for e in range(1 , 6):
    append_by_me(num , e)
print(num)

# class Example 
def list_by_order(n):
    empty_list = []
    for e in range(1 , n+1):
        empty_list.append(e)
    return empty_list

print(list_by_order(10))

# class Example 
def remove_element(L, n):
    """
    L is list,
    and n is the number that has been removed from the list
    """
    empty_list = []
    for i in L:
        if i != n:
            empty_list.append(i)
    return empty_list

list_for_removig_element = [1 , 2 , 2 ,3, 3 ,3 , 4 ,4 ,4 ,4]
print(remove_element(list_for_removig_element , 2))
print(remove_element(list_for_removig_element , 3))


