# Program to assign grade based on marks

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "Grade A"
elif marks >= 75:
    grade = "Grade B"
elif marks >= 50:
    grade = "Grade C"
else:
    grade = "Grade D"

print("\n----- Output -----")
print("Marks Entered:", marks)
print("Assigned Grade:", grade)

#OUTPUT
"""Enter your marks: 56

----- Output ----- 
Marks Entered: 56.0
Assigned Grade: Grade C"""