# Check if tuple elements are unique

n = int(input("Enter size: "))  # size
t = tuple(int(input("Enter element: ")) for i in range(n))  # tuple

print("\n----- Output -----")  # output section
if len(t) == len(set(t)):  # compare lengths
    print("All elements are Unique")
else:
    print("Elements are Not Unique")
    #OUTPUT
    """
    Enter size: 3
Enter element: 5
Enter element: 67
Enter element: 3

----- Output -----
All elements are Unique
"""