age = int(input("Enter age: "))
heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ")
severe_injury = input("Is there severe injury? (yes/no): ")

if heart_rate_abnormal.lower() == "yes" or severe_injury.lower() == "yes":
    condition = "Critical"
else:
    condition = input("Enter condition (moderate/normal): ").lower()

# Upgrade if age > 65 and moderate
if age > 65 and condition == "moderate":
    condition = "Critical"

print("Patient Category:", condition.capitalize())