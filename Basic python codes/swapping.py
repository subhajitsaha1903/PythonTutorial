# swapping of two numbers using a third variable
x = int(input("Enter the first Number: "))
y = int(input("Enter the second Number: "))

# z = x+y
# y = z-y
# x = z-y

x, y = y, x
print("The swapped numbers using third variable are respectively", x, "and", y)
