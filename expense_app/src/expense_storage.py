"""Saves and opens expenses."""
import json


def expense_to_dict(expense):
    """Turn one expense into a dictionary."""
    return {
        'date': str(expense.expense_date),
        'category': expense.category,
        'description': expense.description,
        'amount': expense.amount,
    }


def save_expenses(expenses, file_name):
    """Write all the expenses to a JSON file."""
    expense_list = []
    for expense in expenses:
        expense_list.append(expense_to_dict(expense))
    with open(file_name, 'w') as f:
        f.write(json.dumps(expense_list))

