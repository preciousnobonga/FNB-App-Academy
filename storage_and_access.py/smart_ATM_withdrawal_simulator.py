# simulate a bank transaction checking if a user has enough money:
# set a fixed variable representing a bank balance, for example: balance = 500
# ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!)
# if the request is less than or equal to the balance, deduct the amount and print:
# "Withdrawal successful! Remaining balance: RX"
# Otherwise (else) print: "Declined. Insufficient funds"

# set a fixed variable representing a bank balance
balance = 1000

# ask the user how much money they want to withdraw
withdraw_amount = float(input("Enter the amount to withdraw: "))

# "Withdrawal successful! Remaining balance: RX"
if withdraw_amount <= balance:
    balance -= withdraw_amount
    print(f"Withdrwal succesful! Remaining balance: R{balance:}")
else:
    print("Declined. Insufficient funds.")
    