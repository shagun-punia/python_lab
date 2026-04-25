# Intersection of two sets

n1 = int(input("Enter size of first set: "))  # size1
s1 = set(int(input("Enter element: ")) for i in range(n1))  # set1

n2 = int(input("Enter size of second set: "))  # size2
s2 = set(int(input("Enter element: ")) for i in range(n2))  # set2

print("\n----- Output -----")  # output
print("Intersection:", s1 & s2)  # intersection
#OUTPUT
"""
Enter size of first set: 2
Enter element: 56
Enter element: 67
Enter size of second set: 3
Enter element: 56
Enter element: 67
Enter element: 9

----- Output -----
Intersection: {56, 67}
"""