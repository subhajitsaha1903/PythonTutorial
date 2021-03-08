'''
n = int(input("Enter the row value: "))
for i in range(1, n+1, 1):
    print("# # # #")
    i += 1
'''
n = int(input("Enter the row value: "))

for i in range(n):
    for j in range(n-i):
        print("#", end=" ")
        j = j+1
    print()
    i += 1
