
import json

EXPENSES_FILE = "week-01/expenses.json"
APPROVAL_LIMIT = 25000


def load_expenses(path):
    with open(path, "r") as file:
        expenses = json.load(file)
    return expenses


def category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    return totals


def format_rupees(amount):
    return f"Rs. {amount:,}"


def main():
    expenses = load_expenses(EXPENSES_FILE)

    expense_count = len(expenses)

    total = 0
    for expense in expenses:
        total += expense["amount"]

    totals = category_totals(expenses)

    largest = expenses[0]
    approval_expenses = []

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

        if expense["amount"] > APPROVAL_LIMIT:
            approval_expenses.append(expense)

    print("CAFE EXPENSE REPORT")
    print("-------------------")

    print("Number of expenses:", expense_count)
    print("Total spent:", format_rupees(total))

    print("\nCategory Totals:")

    for category in totals:
        print(category + ":", format_rupees(totals[category]))

    print("\nLargest Expense:")
    print(largest["item"], "-", format_rupees(largest["amount"]))

    print("\nExpenses Requiring Approval:")

    for expense in approval_expenses:
        print(expense["item"], "-", format_rupees(expense["amount"]))

    print("Number requiring approval:", len(approval_expenses))

    summary = {
        "expense_count": expense_count,
        "total": total,
        "by_category": totals
    }

    with open("week-01/summary.json", "w") as file:
        json.dump(summary, file, indent=4)


main()

