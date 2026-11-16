"""Filters expenses by category and by date."""


def filter_by_category(expenses, category):
    """Get the expenses that have this category."""
    matches = []
    for expense in expenses:
        if expense.category.lower() == category.lower():
            matches.append(expense)
    return matches