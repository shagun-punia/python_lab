# Sum of digits using function

def sum_digits(num):  # define function
    total = 0  # store sum
    while num > 0:  # loop till 0
        digit = num % 10  # get digit
        total += digit  # add digit
        num = num // 10  # remove digit
    return total  # return sum

num = int(input("Enter a number: "))  # input

print("\n----- Output -----")
print("Sum of digits is:", sum_digits(num))  # print result
#OUTPUT
"""
Enter a number: 99

----- Output -----
Sum of digits is: 18
"""