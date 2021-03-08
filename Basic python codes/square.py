n = int(input("Enter the row value: "))

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        print("#", end=" ")
        j = j+1
    print()
    i += 1
