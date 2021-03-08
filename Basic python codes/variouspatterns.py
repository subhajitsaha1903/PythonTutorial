# printing a triangle pattern, containing odd number of * in each row i.e. 1,3,5,7,9,11,13

num = int(input("Enter the number of rows: "))

k = 1
for i in range(1, num+1):
    for j in range(1, k+1):
        print("*", end=" ")
    k = k+2
    print()
    #i = i+1
