# Program: Tuple and String Combined Example
# This program takes a sentence from the user,
# converts it into words, stores them in a tuple,
# and performs basic operations.

# Taking input from user
sentence = input("Enter a sentence: ")

# Splitting sentence into words
words_list = sentence.split()

# Converting list into tuple
words_tuple = tuple(words_list)

# Displaying results
print("\n----- Output -----")
print("Sentence Entered:", sentence)
print("Words in Tuple:", words_tuple)
print("Total Words:", len(words_tuple))

#OUTPUT
"""Enter a sentence: I thought to go to Delhi

----- Output -----
Sentence Entered: I thought to go to Delhi
Words in Tuple: ('I', 'thought', 'to', 'go', 'to', 'Delhi')
Total Words: 6"""