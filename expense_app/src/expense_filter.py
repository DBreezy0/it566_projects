"""Filters expenses by category and by date."""


def filter_by_category(expenses, category):
    """Get the expenses that have this category."""
    matches = []
    for expense in expenses:
        if expense.category.lower() == category.lower():
            matches.append(expense)
    return matches


def filter_by_date_range(expenses, start_date, end_date):
    """Get the expenses between two dates, including both dates."""
    matches = []
    for expense in expenses:
        if expense.expense_date >= start_date and expense.expense_date <= end_date:
            matches.append(expense)
    return matches