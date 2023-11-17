from expense import Expense
import calendar
import datetime

def main():
    print(f" 📌 Running Expense Tracker ")
    expenses_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense.
    expense = get_user_expense()

    # Write the expense to a file.
    save_expense_to_file(expense, expenses_file_path)
    
    # Read the file and Summarize the expenses.
    summarize_expense(expenses_file_path, budget)


def get_user_expense():
    print(f" 📌 Getting User Expense ")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "🍔 Food",
        "🏘️ Home",
        "🏢 Work",
        "🎉 Fun",
        "✨ Misc"
    ]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name} ")

        value_range = f"[1- {len(expense_categories)}]"
        selected_index = int(input(f"Select a category number: {value_range} ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount= expense_amount  )
            return new_expense
        else:
            print("Incorrect Category, plz try again!")
        
def save_expense_to_file(expense, expenses_file_path):
    print(f" 📌 Saving User Expense {expense} to {expenses_file_path}")
    with open(expenses_file_path, "a") as f:
         f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

def summarize_expense(expenses_file_path, budget):
    print(f" 📌 Summarizing User Expense ")
    expenses: list[Expense] = []
    with open(expenses_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            #unpack values from a comma-separated line and assigns those values to the variables expense_name, expense_category, and expense_amount
            ## Using the strip() method to remove leading and trailing whitespaces, then using split(",") to split the string into a list based on commas
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense (
                name=expense_name,
                amount=float(expense_amount), 
                category= expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expenses by category 〽️:")
    for key, amount in amount_by_category.items():
        print(f"   {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total spent ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget remaining ${remaining_budget:.2f}")

    # Get the current date
    current_date = datetime.date.today()
    # Get the last day of the current month
    last_day_of_month = calendar.monthrange(current_date.year, current_date.month)[1]
    # Calculate the remaining number of days
    remaining_days = last_day_of_month - current_date.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Daily budget ${daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__== "__main__" :
    main()
