# Program: Count frequency of each character in a string using dictionary

# Step 1: Take input string from user
text = input("Enter a string: ")

# Step 2: Create empty dictionary to store frequency
freq = {}

# Step 3: Traverse each character in string
for ch in text:
    # If character already exists, increase count
    if ch in freq:
        freq[ch] += 1
    else:
        # Otherwise add character with count 1
        freq[ch] = 1

# Step 4: Display the frequency dictionary
print("Character frequency:", freq)


#  Output:
"""
Enter a string: hello
Character frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""