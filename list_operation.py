# Program: Perform Multiple List Operations

# Create empty list
numbers = []

# Take input from user
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# 1️⃣ Sum of elements
print("Sum of elements:", sum(numbers))

# 2️⃣ Largest and Smallest element
print("Largest element:", max(numbers))
print("Smallest element:", min(numbers))

# 3️⃣ Count even and odd numbers
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)

# 4️⃣ Sort list
numbers.sort()
print("List in Ascending Order:", numbers)

numbers.sort(reverse=True)
print("List in Descending Order:", numbers)

# 5️⃣ Reverse list
numbers.reverse()
print("Reversed List:", numbers)

# 6️⃣ Search element
search = int(input("\nEnter element to search: "))

if search in numbers:
    print("Element found in the list.")
else:
    print("Element not found.")

# 7️⃣ Remove element
remove_value = int(input("Enter element to remove: "))

if remove_value in numbers:
    numbers.remove(remove_value)
    print("Updated List after removal:", numbers)
else:
    print("Element not found, cannot remove.")
    #OUTPUT
    """Enter number of elements: 4
Enter element: 12
Enter element: 34
Enter element: 43
Enter element: 98

Original List: [12, 34, 43, 98]
Sum of elements: 187
Largest element: 98
Smallest element: 12
Even count: 3
Odd count: 1
List in Ascending Order: [12, 34, 43, 98]
List in Descending Order: [98, 43, 34, 12]
Reversed List: [12, 34, 43, 98]

Enter element to search: 4
Element not found.
Enter element to remove: 12
Updated List after removal: [34, 43, 98]"""