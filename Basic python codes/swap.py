# # swapping of two numbers without using a third variable
# x = int(input("Enter the first Number: "))
# y = int(input("Enter the second Number: "))

# x = x+y
# y = x-y
# x = x-y

# print("The swapped numbers without using third variable are respectively", x, "and", y)


# swapping of two numbers using a third variable
x = int(input("Enter the first Number: "))
y = int(input("Enter the second Number: "))

z = x+y
y = z-y
x = z-y

print("The swapped numbers using third variable are respectively", x, "and", y)
