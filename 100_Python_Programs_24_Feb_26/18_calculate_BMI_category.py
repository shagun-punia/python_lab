# Program to calculate BMI and category

weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\n----- Output -----")
print("BMI:", bmi)
print("Category:", category)
#OUTPUT
"""Enter weight (in kg): 67
Enter height (in meters): 5 
----- Output -----
BMI: 2.68
Category: Underweight"""