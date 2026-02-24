# Check palindrome string

def is_palindrome(text):  # define function
    rev = text[::-1]  # reverse string
    if text == rev:  # compare
        return True
    return False  # not palindrome

text = input("Enter a string: ")  # input

print("\n----- Output -----")
if is_palindrome(text):  # call function
    print("It is Palindrome")
else:
    print("It is not Palindrome")

#OUTPUT
"""
Enter a string: mom

----- Output -----
It is Palindrome
"""