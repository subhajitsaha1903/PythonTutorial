# n != n.(n-1).(n-2).(n-3)......1
# n != n.(n-1)!
# n != n.(n-1).(n-2)!
# ..........

def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
    return fact


n = int(input("Enter the number: "))

print("Factorial of", n, "is:", factorial(n))
