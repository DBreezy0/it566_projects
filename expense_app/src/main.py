"""Serves as the point of entry to the Expense Tracker."""
import sys
from datetime import date
from expense import Expense
from expense_storage import save_expenses, open_expenses
from expense_filter import filter_by_category, filter_by_date_range


def display_menu():
    """Prints menu items to the console."""
    print('\n\t\tExpense Tracker\n')
    print('\t1. Add an expense')
    print('\t2. Print all expenses')
    print('\t3. Save expenses to a file')
    print('\t4. Open expenses from a file')
    print('\t5. Filter expenses')
    print('\t6. Exit')


def text_to_date(date_text):
      """Turn the date the user types into a real date."""
      date_parts = date_text.split('/')
      month = int(date_parts[0])
      day = int(date_parts[1])
      year = int(date_parts[2])
      return date(year=year, month=month, day=day)


def add_expense(expenses):
     """Add one expense to the list."""
     expense_date = text_to_date(input('\n\tDate (mm/dd/yyyy): '))
     category = input('\tCategory: ')
     description = input('\tDescription: ')
     amount = float(input('\tAmount: '))
     expenses.append(Expense(expense_date, category, description, amount))
     print('\tExpense added.')


def print_expenses(expenses):
    """Print every expense in the list."""
    print('')
    if len(expenses) == 0:
        print('\tNo expenses yet.')
    for expense in expenses:
        print(f'\t{expense}')


def save_to_file(expenses):
    """Ask for a file name and save the expenses."""
    file_name = input('\n\tFile name (example: expenses.json): ')
    save_expenses(expenses, file_name)
    print(f'\tSaved {len(expenses)} expense(s) to {file_name}.')


def open_from_file(expenses):
    """Ask for a file name and load the expenses from it."""
    file_name = input('\n\tFile name: ')
    try:
        opened_expenses = open_expenses(file_name)
        expenses.clear()
        expenses.extend(opened_expenses)
        print(f'\tOpened {len(expenses)} expense(s) from {file_name}.')
    except Exception as e:
        print(f'\n\tProblem opening the file: {e}')


def filter_expenses(expenses):
    """Ask what to filter by and print the matching expenses."""
    category = input('\n\tCategory (press Return to skip): ')
    start_text = input('\tStart date mm/dd/yyyy (press Return to skip): ')
    end_text = input('\tEnd date mm/dd/yyyy (press Return to skip): ')
    try:
        matches = expenses
        if category != '':
            matches = filter_by_category(matches, category)
        if start_text != '' and end_text != '':
            start_date = text_to_date(start_text)
            end_date = text_to_date(end_text)
            matches = filter_by_date_range(matches, start_date, end_date)
        print_expenses(matches)
    except Exception as e:
        print(f'\n\tProblem filtering: {e}')


def process_menu_choice(expenses):
    """Reads the choice and runs the command."""
    menu_choice = input('\n\tEnter Command Number: ')
    match menu_choice:
        case '1': add_expense(expenses)
        case '2': print_expenses(expenses)
        case '3': save_to_file(expenses)
        case '4': open_from_file(expenses)
        case '5': filter_expenses(expenses)
        case '6': sys.exit()
        case _: print(f'\n\t{menu_choice} is not a command.')


def main():
    """Start the Expense Tracker."""
    expenses = []
    while True:
        display_menu()
        process_menu_choice(expenses)


if __name__ == '__main__':
    main()