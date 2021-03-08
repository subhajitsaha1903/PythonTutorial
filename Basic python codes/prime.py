n = int(input("Enter the value: "))

for i in range(2, n):
    if ((n % i) == 0):
        print("NOT a prime number i.e. Composite Number")
        break
else:
    print("Prime Number")
