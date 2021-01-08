def f(x):
    
    return x % 2 != 0 and x % 3 != 0


#using filter function
r = filter(f,range(1, 100))
print(list(r))
