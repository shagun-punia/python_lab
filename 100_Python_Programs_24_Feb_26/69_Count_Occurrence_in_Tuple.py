# Count occurrence in tuple

n = int(input("Enter size: "))  # size
t = tuple(int(input("Enter element: ")) for i in range(n))  # tuple

element = int(input("Enter element to count: "))  # input element

print("\n----- Output -----")  # output section
print("Count:", t.count(element))  # print count
#OUTPUT
"""
Enter size: 3
Enter element: 67
Enter element: 89
Enter element: 7
Enter element to count: 7

----- Output -----
Count: 1
"""