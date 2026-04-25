# Student marks dictionary and topper

n = int(input("Enter number of students: "))  # number

marks = {}  # empty dictionary

for i in range(n):  # input loop
    name = input("Enter student name: ")  # name
    mark = int(input("Enter marks: "))  # marks
    marks[name] = mark  # store data

topper = max(marks, key=marks.get)  # find topper

print("\n----- Output -----")  # output
print("Topper is:", topper)  # print topper
#OUTPUT
"""
Enter number of students: 3
Enter student name: ram
Enter marks: 45
Enter student name: shyam
Enter marks: 90
Enter student name: krishna
Enter marks: 67

----- Output -----
Topper is: shyam
"""