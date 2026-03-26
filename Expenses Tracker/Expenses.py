def add_expense(balance):
    while True:
        expense_name = input("Enter expense name (or type 'done' to finish): ").strip()
        if expense_name.lower() == 'done':
            break
        try:
            expense_amount = float(input(f"Enter amount for {expense_name}: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if expense_amount > balance:
            print("Warning! Expense exceeds current balance.")
        else:
            balance -= expense_amount
            print(f"Expense added. Remaining balance: {balance:.2f}")
    
    return balance

def main():
    try:
        income = float(input("Enter your monthly income: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    balance = income
    print(f"Your starting balance is: {balance:.2f}\n")
    
    balance = add_expense(balance)
    
    print(f"\nFinal balance: {balance:.2f}")
    print("Thank you for using Expense Tracker!")

main()