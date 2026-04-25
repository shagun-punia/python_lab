# creating a blank list
numbers = []

# take number of elements
n = int(input("enter number of elements: "))

# ask for elements
for i in range(n):
    num = int(input("enter a number: "))
    print("-------------")
    numbers.append(num)

print("numbers are:", numbers)

sum = 0

for num in numbers:
    sum = sum + num

print("Sum is:", sum)
#OUTPUT
"""enter number of elements: 9
enter a number: 4
-------------   
enter a number: 7
-------------
enter a number: 9
-------------
enter a number: 0
-------------
enter a number: 6
-------------
enter a number: 8
-------------
enter a number: 5
-------------
enter a number: 8
-------------
enter a number: 4
-------------
numbers are: [4, 7, 9, 0, 6, 8, 5, 8, 4]
Sum is: 51"""
