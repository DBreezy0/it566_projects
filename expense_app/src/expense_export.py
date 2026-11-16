"""Exports expenses to a CSV file that opens in Excel."""


def export_to_csv(expenses, file_name):
    """Write all the expenses to a CSV file."""
    with open(file_name, 'w') as f:
        f.write('Date,Category,Description,Amount\n')
        for expense in expenses:
            f.write(f'{expense.expense_date},"{expense.category}",'
                    f'"{expense.description}",{expense.amount:.2f}\n')