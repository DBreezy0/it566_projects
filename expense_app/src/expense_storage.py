"""Saves and opens expenses."""


def expense_to_dict(expense):
    """Turn one expense into a dictionary."""
    return {
        'date': str(expense.expense_date),
        'category': expense.category,
        'description': expense.description,
        'amount': expense.amount,
    }