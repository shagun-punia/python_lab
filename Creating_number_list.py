# creating a numeric list of 5 numbers
numbers = [23, 45, 67, 85, 43]

# printing list
print(numbers)

# access particular element
print(numbers[3])

# displaying without square brackets
print("numbers are:")
print(*numbers)

# using for loop
for num in numbers:
    print(num)

# length of list
length = len(numbers)
print("length of a list:", length)

# reverse order
for index in range(length - 1, -1, -1):
    print(numbers[index], end=" ")

# sum of elements
sum = 0
for num in numbers:
    sum += num
print("\nsum of all numbers in list:", sum)

# find maximum element
max = numbers[0]
for index in range(1, length):
    if max < numbers[index]:
        max = numbers[index]

print("maximum number is:", max)
#output
"""[23, 45, 67, 85, 43]
85
numbers are:
23 45 67 85 43
23
45
67
85
43
length of a list: 5
43 85 67 45 23
sum of all numbers in list: 263
maximum number is: 85"""