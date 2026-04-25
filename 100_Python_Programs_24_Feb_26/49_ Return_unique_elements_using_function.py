# Return unique elements from a list

def unique_elements(lst):  # function to get unique values
    unique = []
    for item in lst:  # check each element
        if item not in unique:
            unique.append(item)
    return unique

n = int(input("How many elements? "))  # input size
lst = []

for i in range(n):  # taking list input
    lst.append(int(input("Enter element: ")))

print("\n----- Output -----")
print("Original List:", lst)
print("Unique Elements:", unique_elements(lst))
#OUTPUT
"""
How many elements? 5
Enter element: 4
Enter element: 6
Enter element: 3
Enter element: 5
Enter element: 4

----- Output -----
Original List: [4, 6, 3, 5, 4]
Unique Elements: [4, 6, 3, 5]
"""