# Separate even and odd numbers

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

even = []
odd = []

for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("\n----- Output -----")
print("Even Numbers:", even)
print("Odd Numbers:", odd)
#OUTPUT
"""
How many elements? 4
Enter element: 7
Enter element: 9
Enter element: 0
Enter element: 2

----- Output -----
Even Numbers: [0, 2]
Odd Numbers: [7, 9]
"""