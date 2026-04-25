# Sort list without using sort()

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

# simple bubble sort
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("\n----- Output -----")
print("Sorted List:", lst)
#OUTPUT
"""
How many elements? 3
Enter element: 67
Enter element: 78
Enter element: 67

----- Output -----
Sorted List: [67, 67, 78]
"""