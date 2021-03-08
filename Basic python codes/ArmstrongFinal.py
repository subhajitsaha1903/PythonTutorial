# printing the number of digits present in a given number
num_str = input("Enter a number: ")
num = int(num_str)
# print(type(num))
# print(len(num))
x = len(num_str)


# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** x
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
