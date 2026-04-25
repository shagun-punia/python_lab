# Program: Find common elements between two lists without using set

# Step 1: Take input for first list
list1 = list(map(int, input("Enter first list elements: ").split()))

# Step 2: Take input for second list
list2 = list(map(int, input("Enter second list elements: ").split()))

# Step 3: Create empty list to store common elements
common = []

# Step 4: Traverse first list
for item in list1:
    # Check if element is in second list and not already added
    if item in list2 and item not in common:
        common.append(item)

# Step 5: Display result
print("Common elements:", common)

#output
"""
Enter first list elements: 5 7 3 67
Enter second list elements: 78 45 3 7
Common elements: [7, 3]
"""