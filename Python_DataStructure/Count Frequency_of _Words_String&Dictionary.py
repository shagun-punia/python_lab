# Program: Count Frequency of Words
# This program takes a sentence from the user
# and counts how many times each word appears
# using a dictionary.

# Taking input from user
sentence = input("Enter a sentence: ")

# Converting sentence into words
words = sentence.split()

# Creating empty dictionary
frequency = {}

# Counting word frequency
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Displaying results
print("\n----- Output -----")
print("Sentence Entered:", sentence)
print("Total Words:", len(words))
print("Word Frequency Dictionary:")
print(frequency)

#OUTPUT
"""Enter a sentence: My name is ram ram

----- Output -----
Sentence Entered: My name is ram ram
Total Words: 5
Word Frequency Dictionary:
{'My': 1, 'name': 1, 'is': 1, 'ram': 2}"""
