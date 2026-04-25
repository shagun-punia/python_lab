# Program: Count Words in a String
# This program takes a sentence from the user
# and counts the total number of words in it.

# Taking input from user
sentence = input("Enter a sentence: ")

# Splitting the sentence into words
words = sentence.split()

# Counting total words
total_words = len(words)

# Displaying results in clear format
print("\n----- Output -----")
print("Sentence Entered:", sentence)
print("Words in Sentence:", words)
print("Total Number of Words:", total_words)


#OUTPUT
"""Enter a sentence: my name is shagun punia

----- Output -----
Sentence Entered: my name is shagun punia
Words in Sentence: ['my', 'name', 'is', 'shagun', 'punia']
Total Number of Words: 5"""