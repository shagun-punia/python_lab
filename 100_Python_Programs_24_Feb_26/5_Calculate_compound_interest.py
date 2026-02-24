# Program to calculate Compound Interest

# Taking input from user
principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest (in %): "))
time = float(input("Enter the Time (in years): "))

# Calculating total amount using Compound Interest formula
amount = principal * (1 + rate/100) ** time

# Calculating compound interest
compound_interest = amount - principal

# Displaying the result
print("\n----- Output -----")
print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time (in years):", time)
print("Total Amount:", amount)
print("Compound Interest is:", compound_interest)
#OUTPUT
"""Enter the Principal Amount: 3400
Enter the Rate of Interest (in %): 5
Enter the Time (in years): 6

----- Output -----
Principal Amount: 3400.0
Rate of Interest: 5.0 %
Time (in years): 6.0
Total Amount: 4556.325178125001
Compound Interest is: 1156.325178125001"""