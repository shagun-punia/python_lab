# Program to find minimum value in dictionary

print("How many elements?")
n = int(input())

d = {}

for i in range(n):
    print("Enter key:")
    key = input()
    
    print("Enter value (number only):")
    value = int(input())
    
    d[key] = value

if n > 0:
    min_value = min(d.values())
    
    for k in d:
        if d[k] == min_value:
            print("Minimum value is:", min_value)
            print("Key of minimum value is:", k)
else:
    print("Dictionary is empty")
    #OUTPUT
    """
    How many elements?
2
Enter key:
a
Enter value (number only):
45
Enter key:
b
Enter value (number only):
67
Minimum value is: 45
Key of minimum value is: a
"""