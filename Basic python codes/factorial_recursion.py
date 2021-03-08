# recursion  - factorial of a number

def factorial_using_recursion(n):
    fact = 1
    if (n == 0 or n == 1):
        return 1
    else:
        fact = n*factorial_using_recursion(n-1)
        return fact


n = int(input("Enter the number: "))
print("Factorial of", n, "is", factorial_using_recursion(n))
