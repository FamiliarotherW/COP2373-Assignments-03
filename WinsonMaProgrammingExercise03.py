# WinsonMaProgrammingExercise03.py

from functools import reduce

def get_expenses():
    # Monthly expesnes from user
    expenses = []
    
    while True:
        expense_type = input("Enter expense type (or type 'done'): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input("Enter amount: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Enter a number. ")
    return expenses
    
def analyze_expenses(expenses):
    # Anayze expenses
    # Hanldes when there's no expenses
    if not expenses: 
        return 0, None, None
        
    total_expense = reduce (lambda acc, item: acc + item [1], expenses, 0)
    
    highest_expense = reduce(lambda acc, item: item if item[1] > acc[1] else acc, expenses)
    lowest_expense = reduce(lambda acc, item: item if item[1] < acc[1] else acc, expenses)
    
    return total_expense, highest_expense, lowest_expense
    
def main():
    expenses = get_expenses()
    total, highest, lowest = analyze_expenses(expenses)
    
    print("\n--- Expense Summary ---")
    if total == 0:
        print("No expenses.")
    else:
        print(f"Total: ${total:.2f}")
        print(f"Highest: {highest[0]} (${highest[1]:.2f})")
        print(f"Lowest: {lowest[0]} (${lowest[1]:.2f})")
        
if __name__ == "__main__":
    main()
