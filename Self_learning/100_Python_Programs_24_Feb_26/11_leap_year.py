# Program to check whether a given year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "It is a Leap Year."
else:
    result = "It is not a Leap Year."

print("\n----- Output -----")
print("Year Entered:", year)
print(result)
#OUTPUT
"""Enter a year: 2024
----- Output -----
Year Entered: 2024
It is a Leap Year."""