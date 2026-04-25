# Count character frequency

text = input("Enter a string: ")  # input

freq = {}  # dictionary

for ch in text:  # loop characters
    freq[ch] = freq.get(ch, 0) + 1  # count frequency

print("\n----- Output -----")  # output
print("Character Frequency:", freq)  # print result
#OUTPUT
"""
Enter a string: moon

----- Output -----
Character Frequency: {'m': 1, 'o': 2, 'n': 1}
"""