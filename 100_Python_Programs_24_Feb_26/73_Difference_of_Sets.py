# Difference of two sets

n1 = int(input("Enter size of first set: "))  # size1
s1 = set(int(input("Enter element: ")) for i in range(n1))  # set1

n2 = int(input("Enter size of second set: "))  # size2
s2 = set(int(input("Enter element: ")) for i in range(n2))  # set2

print("\n----- Output -----")  # output
print("Difference:", s1 - s2)  # difference
#OUTPUT
"""
Enter size of first set: 3
Enter element: 78
Enter element: 9
Enter element: 6
Enter size of second set: 2
Enter element: 67
Enter element: 9

----- Output -----
Difference: {78, 6}
"""