# Program: Find the first non-repeating character in a string

# Step 1: Take input string
text = input("Enter a string: ")

# Step 2: Initialize flag variable
found = False

# Step 3: Traverse each character in string
for ch in text:
    # Check if character appears only once
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        found = True
        break

# Step 4: If no such character found
if not found:
    print("No non-repeating character found")

# Sample Input:
# aabbcde

# Sample Output:
# c