# Find second largest number

n = int(input("How many elements? "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

lst = list(set(lst))  # remove duplicates
lst.sort()

if len(lst) >= 2:
    second_largest = lst[-2]
    print("\n----- Output -----")
    print("Second Largest:", second_largest)
else:
    print("Not enough elements.")
    #OUTPUT
    """
    How many elements? 3
Enter element: 78
Enter element: 78
Enter element: 5

----- Output -----
Second Largest: 5
"""