# Program: Sort a list of tuples based on marks using lambda

# Step 1: Take number of students
n = int(input("Enter number of students: "))

# Step 2: Create empty list
data = []

# Step 3: Take input for each student
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    # Add tuple (name, marks) to list
    data.append((name, marks))

# Step 4: Sort list using lambda function (based on marks)
data.sort(key=lambda x: x[1])

# Step 5: Display sorted list
print("Sorted list:", data)

#output:Enter number of students: 3
"""
Enter name: ram
Enter marks: 45
Enter name: sam
Enter marks: 78
Enter name: abhay
Enter marks: 98
Sorted list: [('ram', 45), ('sam', 78), ('abhay', 98)]"""
