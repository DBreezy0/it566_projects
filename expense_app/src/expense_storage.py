"""Saves and opens expenses."""
import json
from datetime import date
from expense import Expense


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


def dict_to_expense(expense_dict):
    """Make an expense from the saved data."""
    date_parts = expense_dict['date'].split('-')
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    return Expense(date(year=year, month=month, day=day),
                   expense_dict['category'],
                   expense_dict['description'],
                   expense_dict['amount'])


def open_expenses(file_name):
    """Open a saved file and get the expenses from it."""
    with open(file_name, 'r') as f:
        expense_list = json.loads(f.read())
    expenses = []
    for expense_dict in expense_list:
        expenses.append(dict_to_expense(expense_dict))
    return expenses