# Program 1: Student Marks Analyzer
# This program analyzes student marks.

# Taking input from user
marks = list(map(int, input("Enter student marks separated by space: ").split()))

# Removing invalid marks (less than 0 or greater than 100)
valid_marks = [m for m in marks if 0 <= m <= 100]

if len(valid_marks) == 0:
    print("\nNo valid marks entered.")
else:
    # Calculating average
    average = sum(valid_marks) / len(valid_marks)

    # Finding topper
    topper = max(valid_marks)

    # Displaying results
    print("\n----- Result Summary -----")
    print("Valid Marks:", valid_marks)
    print("Average Marks:", round(average, 2))
    print("Topper Marks:", topper)

    # Assigning grade
    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
        #OUTPUT
        """Enter student marks separated by space: 12 
68 98 49 78

----- Result Summary -----
Valid Marks: [12, 68, 98, 49, 78]
Average Marks: 61.0
Topper Marks: 98
Grade: B"""
