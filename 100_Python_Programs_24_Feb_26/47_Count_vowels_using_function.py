# Count vowels using function

def count_vowels(text):  # define function
    count = 0  # counter
    for ch in text:  # loop string
        if ch in "aeiouAEIOU":  # check vowel
            count += 1  # increase count
    return count  # return value

text = input("Enter a string: ")  # input

print("\n----- Output -----")
print("Number of vowels:", count_vowels(text))  # print result

#OUTPUT
"""
Enter a string: punia

----- Output ----- 
Number of vowels: 3
"""