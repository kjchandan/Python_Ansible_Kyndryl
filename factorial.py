n = int(input("Enter the Number: "))

import sys
print(sys.argv)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
    
# print(factorial(int(sys.argv[1])))


print(factorial(n))

# print(factorial(0))
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
