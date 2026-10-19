def quoitent_And_remainder(x , y):
    q = x // y
    r = x % y
    return (q , r)

both = quoitent_And_remainder( 1 , 3)

(quot , rem) = quoitent_And_remainder(5  ,2)

print(quot , rem)