# Program to delete a key from dictionary

print("How many elements?")  # ask size
n = int(input())  # take number

d = {}  # empty dictionary

for i in range(n):  # loop for input
    print("Enter key:")  # ask key
    key = input()  # take key
    
    print("Enter value:")  # ask value
    value = input()  # take value
    
    d[key] = value  # store in dictionary

print("Enter key to delete:")  # ask delete key
delete_key = input()  # take key

if delete_key in d:  # check key exists
    del d[delete_key]  # delete key
    print("Updated Dictionary:")  # heading
    for k in d:
        print(k, d[k])  # print remaining items
else:
    print("Key not found")  # if key not present
    #OUTPUT
    """
    How many elements?
2
Enter key:
a
Enter value:
89
Enter key:
c  
Enter value:
45
Enter key to delete:
c
Updated Dictionary:
a 89
"""