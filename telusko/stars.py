# subhajit saha
n = int(input("How Many Rows You Want To Print: "))
boolean_value = bool(int(input("Type 1 Or 0: ")))
# print(type(boolean_value))

if boolean_value == True:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
# elif new == False:
#     for i in range(one, 0, -1):
#         for j in range(1, i+1):
#             print("*", end="")
#         print()
# elif boolean_value == False:
#     for i in range(n, 0, -1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()

# print(boolean_value)
else:
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
