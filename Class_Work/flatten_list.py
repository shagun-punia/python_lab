# Program: Flatten a nested list

# Step 1: Take nested list input
nested = eval(input("Enter nested list: "))

# Step 2: Create empty list to store flattened elements
flat = []

# Step 3: Traverse nested list and append elements
for sublist in nested:
    for item in sublist:
        flat.append(item)

# Step 4: Display result
print("Flattened list:", flat)

#  Output:
"""
Enter nested list: [[1,2],[3,4],[5]]
Flattened list: [1, 2, 3, 4, 5]
"""