
from datetime import datetime
from expense import Expense
from storage import load_expenses, save_expenses


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount (Rs.): "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        if not date:
            return datetime.today().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")


def add_expense(expenses):
    print("\n--- Add New Expense ---")

    amount = get_amount()
    category = input("Enter category (e.g. Food, Travel): ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    date = get_date()
    description = input("Enter description: ").strip()

    expense = Expense(amount, category, date, description)
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"\nExpense #{number}")
        expense.display()


def show_summary(expenses):
    print("\n--- Expense Summary ---")

    if not expenses:
        print("No expenses available for summary.")
        return

    total = sum(expense.amount for expense in expenses)
    print(f"Total expenses: Rs. {total:.2f}")

    category_totals = {}

    for expense in expenses:
        category = expense.category.title()
        category_totals[category] = (
            category_totals.get(category, 0) + expense.amount
        )

    print("\nCategory-wise spending:")

    for category, amount in category_totals.items():
        print(f"{category}: Rs. {amount:.2f}")


def search_expenses(expenses):
    print("\n--- Search Expenses ---")
    keyword = input("Enter category or description to search: ").strip().lower()

    if not keyword:
        print("Please enter a search term.")
        return

    matches = [
        expense for expense in expenses
        if keyword in expense.category.lower()
        or keyword in expense.description.lower()
    ]

    if not matches:
        print("No matching expenses found.")
        return

    for number, expense in enumerate(matches, start=1):
        print(f"\nResult #{number}")
        expense.display()


def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)
        save_expenses(expenses)

        print(f"Deleted expense: {removed.category}")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Expense Summary")
        print("4. Search Expenses")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            search_expenses(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
