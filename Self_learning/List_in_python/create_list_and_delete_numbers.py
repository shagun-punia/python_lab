#create 20 numbers list and delete that
numbers = [1, 5, 3, 7, 5, 9, 2, 5, 8, 6, 5, 4, 10, 5, 11, 12, 5, 13, 14, 5]

print("Original List:")
print(numbers)

num = int(input("Enter a number to delete its extra occurrences: "))

if num in numbers:
    first_index = numbers.index(num)

    while num in numbers:
        numbers.remove(num)

    numbers.insert(first_index, num)

    print("Updated List:")
    print(numbers)
else:
    print("Number not found in the list.")
    
    #OUTPUT
    """Original List:
[1, 5, 3, 7, 5, 9, 2, 5, 8, 6, 5, 4, 10, 5, 11, 12, 5, 13, 14, 5]
Enter a number to delete its extra occurrences: 5
Updated List:
[1, 5, 3, 7, 9, 2, 8, 6, 4, 10, 11, 12, 13, 14]"""