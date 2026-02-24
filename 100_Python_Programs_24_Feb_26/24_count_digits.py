# Count digits in a number

num = int(input("Enter a number: "))  # input
count = 0  # counter
temp = abs(num)  # handle negative

if temp == 0:  # if number is 0
    count = 1
else:
    while temp > 0:  # loop till 0
        count += 1  # increase count
        temp = temp // 10  # remove digit

print("\n----- Output -----")
print("Total digits:", count)  # display

#OUTPUT
"""Enter a number: 56

----- Output -----
Total digits: 2   """