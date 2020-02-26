def f(x):
    
    return x % 2 != 0 and x % 3 != 0


#using filter function
print(filter(f, range(1, 100)))
