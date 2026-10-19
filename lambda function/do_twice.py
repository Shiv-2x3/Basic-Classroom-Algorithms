def do_twice(n , fn):
    return fn(fn(n))

print(do_twice(2 , lambda x:x **2))