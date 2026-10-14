# We define a Function
def is_even(i): # is_even is name for this function
    '''
    consider i as an input.  
    This function checks for wheather this is an even number or not 
    '''
    return i % 2 == 0 

is_even(3) # Calling / Invoking this function

# print(is_even(3))
# is_even(5)

for i in range( 1 , 11):
    if is_even(i):
        print(i , "Even")
    else:
        print(i , "Odd")