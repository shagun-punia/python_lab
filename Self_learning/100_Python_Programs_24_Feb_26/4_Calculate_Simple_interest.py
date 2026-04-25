# Program to calculate Simple Interest

# Taking input from user
principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest (in %): "))
time = float(input("Enter the Time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("\n----- Output -----")
print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time (in years):", time)
print("Simple Interest is:", simple_interest)

#OUTPUT
"""Enter the Principal Amount: 4500
Enter the Rate of Interest (in %): 34
Enter the Time (in years): 5

----- Output -----
Principal Amount: 4500.0
Rate of Interest: 34.0 %
Time (in years): 5.0
Simple Interest is: 7650.0"""