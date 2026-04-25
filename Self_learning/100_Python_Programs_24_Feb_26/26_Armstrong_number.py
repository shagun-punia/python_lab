# Check Armstrong number

num = int(input("Enter a number: "))  # input
temp = num  # copy number
power = len(str(num))  # count digits
sum_val = 0  # store sum

while temp > 0:  # loop till 0
    digit = temp % 10  # get digit
    sum_val += digit ** power  # add power
    temp = temp // 10  # remove digit

print("\n----- Output -----")
if sum_val == num:  # compare
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")
    #OUTPUT
    """Enter a number: 153

----- Output -----
153 is Armstrong"""