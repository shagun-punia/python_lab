# Find minimum in tuple

n = int(input("Enter size: "))  # size
t = tuple(int(input("Enter element: ")) for i in range(n))  # tuple input

print("\n----- Output -----")  # output section
print("Minimum Value:", min(t))  # print min
#OUTPUT
"""
Enter size: 3
Enter element: 4
Enter element: 49
Enter element: 45

----- Output -----
Minimum Value: 4
"""