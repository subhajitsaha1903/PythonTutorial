# Python3 implementation of the approach
# counting number of digits in a number
def count_digits(num):
    num = str(num)
    return len(num)


# Driver code
# num = entered number by user
# x = number of digits in number num, which was entered by user
num = int(input("Enter a number: "))
x = count_digits(num)
# print(x)


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
