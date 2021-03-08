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
print(x)
