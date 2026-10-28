"""Serves as the point of entry to the Expense Tracker."""
import sys


def display_menu():
    """Prints menu items to the console."""
    print('\n\t\tExpense Tracker\n')
    print('\t1. Add an expense')
    print('\t2. Print all expenses')
    print('\t3. Exit')


def print_expenses(expenses):
    """Print every expense in the list."""
    print('')
    if len(expenses) == 0:
        print('\tNo expenses yet.')
    for expense in expenses:
        print(f'\t{expense}')

        
def process_menu_choice(expenses):
    """Reads the choice and runs the command."""
    menu_choice = input('\n\tEnter Command Number: ')
    match menu_choice:
        case '1': print('\n\tNot ready yet.')
        case '2': print_expenses(expenses)
        case '3': sys.exit()
        case _: print(f'\n\t{menu_choice} is not a command.')


def main():
    """Start the Expense Tracker."""
    expenses = []
    while True:
        display_menu()
        process_menu_choice(expenses)


if __name__ == '__main__':
    main()