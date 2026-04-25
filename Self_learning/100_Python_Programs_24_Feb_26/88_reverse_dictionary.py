# Program to reverse a dictionary (swap key and value)

print("How many elements?")
n = int(input())

d = {}
rev = {}

for i in range(n):
    print("Enter key:")
    key = input()
    
    print("Enter value:")
    value = input()
    
    d[key] = value

# reversing dictionary
for k in d:
    rev[d[k]] = k

print("Original Dictionary:", d)
print("Reversed Dictionary:", rev)
#OUTPUT
"""
How many elements?
2
Enter key:
a
Enter value:
23
Enter key:
b
Enter value:
90
Original Dictionary: {'a': '23', 'b': '90'}
Reversed Dictionary: {'23': 'a', '90': 'b'}
"""