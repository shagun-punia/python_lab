balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

if withdraw > 50000:
    print("Error: Daily withdrawal limit is 50,000")
elif withdraw > balance:
    print("Error: Insufficient account balance")
elif withdraw > atm_cash:
    print("Error: ATM does not have enough cash")
else:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)