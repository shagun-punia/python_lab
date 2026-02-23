#create a list of 20 numbers given by user
numbers = []

print("Enter any 20 numbers:")
for i in range(20):
    num = int(input())
    numbers.append(num)

print("---------------------------------------------")

remove_number = int(input("Enter the number you want to remove from the list: "))

print("List is:")
print(numbers)
print("--------------------------------------------------------------------")

# Frequency of number in list
frequency = numbers.count(remove_number)
print("Frequency of", remove_number, "in list:", frequency)

if frequency == 0:
    print(remove_number, "is not present in list")

elif frequency == 1:
    print("As it is unique, it cannot be removed from list")

else:
    print("As it is not a unique number, it will be removed except first occurrence")

    first_found = False
    new_list = []

    for num in numbers:
        if num == remove_number:
            if not first_found:
                new_list.append(num)
                first_found = True
        else:
            new_list.append(num)

    numbers = new_list

print("Updated List:")
print(numbers)

#output
"""1, 5, 3, 7, 5, 9, 2, 5, 8, 6, 5, 4, 10, 5, 11, 12, 5, 13, 14, 12
1
5
3
7
5
9
2
5
8
6
5
4
10
5
11
12
5
13
14
12"""