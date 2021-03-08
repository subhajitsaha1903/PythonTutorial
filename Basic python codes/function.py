# addition and subtraction of two numbers
def add_sub(x, y):
    a = x+y
    b = x-y
    return (a, b)
    # return (b)


x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))
add_sub = add_sub(x, y)
# sub = add_sub(x, y)
print("Summation and Subtraction of", x,
      "and", y, "are respectively:", add_sub)
# print("Subtraction of", x, "and", y, "is:", sub)
