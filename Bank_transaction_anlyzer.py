#  Bank Transaction Analyzer

transactions = list(map(int, input("Enter transactions (+deposit, -withdraw): ").split()))

balance = sum(transactions)

withdrawals = [t for t in transactions if t < 0]

if withdrawals:
    largest_withdrawal = min(withdrawals)
else:
    largest_withdrawal = 0

large_deposits = len([t for t in transactions if t > 10000])

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", large_deposits)