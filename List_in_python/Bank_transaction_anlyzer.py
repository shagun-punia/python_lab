# Program 7: Bank Transaction Analyzer
# This program analyzes bank transactions.
# Positive numbers = Deposits
# Negative numbers = Withdrawals

# Taking user input
transactions = list(map(int, input("Enter transactions (+deposit, -withdraw) separated by space: ").split()))

# Calculate total balance
total_balance = sum(transactions)

# Find largest withdrawal (minimum negative value)
largest_withdrawal = min(transactions)

# Count deposits greater than 10000
big_deposits = len([t for t in transactions if t > 10000])

# Display results
print("\n----- Transaction Summary -----")
print("Transactions Entered:", transactions)
print("Total Balance:", total_balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits greater than 10000:", big_deposits)
#OUTPUT
"""Enter transactions (+deposit, -withdraw) separated by space: +899 -600

----- Transaction Summary -----
Transactions Entered: [899, -600]
Total Balance: 299
Largest Withdrawal: -600
Deposits greater than 10000: 0"""
