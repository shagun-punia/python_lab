# Count vowels in string

text = input("Enter a string: ")  # input
count = 0  # counter

for ch in text:  # loop through string
    if ch in "aeiouAEIOU":  # check vowel
        count += 1  # increase count

print("\n----- Output -----")
print("Number of vowels:", count)  # display

#OUTPUT
"""Enter a string: shagun

----- Output ----- 
Number of vowels: 2
"""