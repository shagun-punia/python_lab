#  Attendance Tracker
attendance = list(map(int, input("Enter attendance (1=Present, 0=Absent) separated by space: ").split()))

# Check if list is empty
if len(attendance) == 0:
    print("No attendance data entered.")

# Check if invalid numbers entered
elif any(x not in [0, 1] for x in attendance):
    print("Invalid input! Please enter only 0 or 1.")

else:
    total_days = len(attendance)
    present_days = sum(attendance)

    percentage = (present_days / total_days) * 100

    print("Total Days:", total_days)
    print("Present Days:", present_days)
    print("Attendance Percentage: {:.2f}%".format(percentage))

    if percentage < 75:
        print("Warning: Attendance below 75%")
    else:
        print("Good! Attendance is satisfactory.")

    # Check consecutive absences
    for i in range(total_days - 1):
        if attendance[i] == 0 and attendance[i + 1] == 0:
            print("Consecutive Absence Warning")
            break
        #output
        """Enter attendance (1=Present, 0=Absent) separated by space: 1 0 1 1 1 0
Total Days: 6
Present Days: 4
Attendance Percentage: 66.67%
Warning: Attendance below 75%"""
