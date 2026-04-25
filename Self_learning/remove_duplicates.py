# Program: Remove duplicates from a list while maintaining order

# Step 1: Take list input
lst = list(map(int, input("Enter elements: ").split()))

# Step 2: Create empty list to store unique elements
unique = []

# Step 3: Traverse list and add elements if not already present
for item in lst:
    if item not in unique:
        unique.append(item)

# Step 4: Display result
print("List without duplicates:", unique)

#  Output:
"""
Enter elements: 1 2 2 3 4 3 5
List without duplicates: [1, 2, 3, 4, 5]
"""