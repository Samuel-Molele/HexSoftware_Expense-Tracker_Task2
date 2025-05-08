from expense import Expense


def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expense.csv"
    # Get user input for expenses
    expense = get_user_expense()
    # Wite their expenses to a file
    save_expense_to_file(expense, expense_file_path)
    
# Function to collect an expense from the user
def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:"))
    expense_categories = [
        "🍔 Food",
        "🏡 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

#Ask user to choose a category
    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int((input(f"Enter a category number {value_range}: "))) -1
        if selected_index in range(len(expense_categories)):

            # If input is valid, create and return an Expense object
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            ) 
            return new_expense
        else:
            print("Invalid category. Please try again")
        break

  # Function to write the expense to a CSV file 
def save_expense_to_file(expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

if __name__ == "__main__":
    main()