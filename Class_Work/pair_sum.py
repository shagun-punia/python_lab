# Program: Find all pairs in a list whose sum equals a target value

# Step 1: Take list input
lst = list(map(int, input("Enter elements: ").split()))

# Step 2: Take target value
target = int(input("Enter target sum: "))

# Step 3: Create empty list for pairs
pairs = []

# Step 4: Traverse list to find pairs
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))

# Step 5: Display result
print("Pairs:", pairs)

#  Output:
"""
Enter elements: 1 2 3 4 5
Enter target sum: 5
Pairs: [(1, 4), (2, 3)]
"""