# Program 1: Student Marks Analyzer

marks = list(map(int, input("Enter marks separated by space: ").split()))

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

if len(valid_marks) == 0:
    print("No valid marks entered.")
else:
    average = sum(valid_marks) / len(valid_marks)
    topper = max(valid_marks)

    print("Valid Marks:", valid_marks)
    print("Average:", average)
    print("Topper:", topper)

    print("Grades:")
    for m in valid_marks:
        if m >= 90:
            print(m, "Grade A")
        elif m >= 75:
            print(m, "Grade B")
        elif m >= 50:
            print(m, "Grade C")
        else:
            print(m, "Fail")