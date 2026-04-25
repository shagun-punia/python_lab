# Program to check whether number lies within a range

num = float(input("Enter a number: "))
lower = float(input("Enter lower limit: "))
upper = float(input("Enter upper limit: "))

if lower <= num <= upper:
    result = "Number lies within the range."
else:
    result = "Number does not lie within the range."

print("\n----- Output -----")
print("Number:", num)
print("Range:", lower, "to", upper)
print(result)
#OUTPUT
"""Enter a number: 45
Enter lower limit: 5
Enter upper limit: 40

----- Output -----
Number: 45.0
Range: 5.0 to 40.0
Number does not lie within the range."""