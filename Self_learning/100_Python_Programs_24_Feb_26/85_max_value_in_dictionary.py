# Program to find maximum value in dictionary

print("How many elements?")  # ask size
n = int(input())  # take number

d = {}  # empty dictionary

for i in range(n):  # loop for input
    print("Enter key:")  # ask key
    key = input()  # take key
    
    print("Enter value (number only):")  # ask value
    value = int(input())  # take value as integer
    
    d[key] = value  # store in dictionary

if n > 0:  # check if dictionary not empty
    max_value = max(d.values())  # find maximum value
    
    for k in d:  # loop to find key of max value
        if d[k] == max_value:
            print("Maximum value is:", max_value)
            print("Key of maximum value is:", k)
else:
    print("Dictionary is empty")
    #OUTPUT
    """
    How many elements?
2
Enter key:
a
Enter value (number only):
7
Enter key:
b
Enter value (number only):
5
Maximum value is: 7
Key of maximum value is: a
"""