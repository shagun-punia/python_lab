# Rotate list by K positions

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

k = int(input("Enter value of K: "))

k = k % n
rotated = lst[k:] + lst[:k]

print("\n----- Output -----")
print("Rotated List:", rotated)
#OUTPUT
"""
How many elements? 4
Enter element: 67
Enter element: 8
Enter element: 45
Enter element: 7
Enter value of K: 2

----- Output -----
Rotated List: [45, 7, 67, 8]
"""