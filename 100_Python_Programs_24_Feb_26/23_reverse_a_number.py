# Reverse a number

num = int(input("Enter a number: "))  # taking input
rev = 0  # store reverse value

while num > 0:  # loop till number becomes 0
    digit = num % 10  # get last digit
    rev = rev * 10 + digit  # build reverse number
    num = num // 10  # remove last digit

print("\n----- Output -----")
print("Reversed number is:", rev)  # print result