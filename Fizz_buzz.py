"""
Given a positive integer, N, print all the integers from 1 to N.

For multiples of 3 print "Fizz" instead of the number and for multiples of 5
print "Buzz". For numbers which are multiples of 3 and 5, print "FizzBuzz".

https://blog.codinghorror.com/why-cant-programmers-program/
"""



def fizz_buzz(n):
    for i in range(1, n+1):
        if i %3 == 0 and i%5 == 0:
            print("FIZZBUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i% 5 == 0:
            print("BUZZ")
        else:
            print(i)



n = 15
print(fizz_buzz(n))
    
