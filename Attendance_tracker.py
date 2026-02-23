#  Attendance Tracker

attendance = list(map(int, input("Enter attendance (1=Present, 0=Absent): ").split()))

if len(attendance) == 0:
    print("No attendance data.")
else:
    percentage = (sum(attendance) / len(attendance)) * 100
    print("Attendance Percentage:", percentage)

    if percentage < 75:
        print("Warning: Below 75%")

    # Check consecutive absences
    for i in range(len(attendance) - 1):
        if attendance[i] == 0 and attendance[i + 1] == 0:
            print("Consecutive Absence Warning")