# Program to validate username and password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    result = "Login Successful."
else:
    result = "Invalid Username or Password."

print("\n----- Output -----")
print(result)

#OUTPUT
"""Enter username: admin
Enter password: 1234

----- Output -----
Login Successful."""