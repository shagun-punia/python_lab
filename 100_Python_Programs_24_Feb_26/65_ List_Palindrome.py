# Check list palindrome

n = int(input("Enter size: "))  # size
lst = [int(input("Enter element: ")) for i in range(n)]  # input

print("\n----- Output -----")  # output section
if lst == lst[::-1]:  # compare with reverse
    print("List is Palindrome")
else:
    print("List is Not Palindrome")
    #OUTPUT
    """
    Enter size: 4
Enter element: 77
Enter element: 88
Enter element: 88
Enter element: 77

----- Output -----
List is Palindrome
"""