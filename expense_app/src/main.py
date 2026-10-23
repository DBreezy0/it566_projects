"""Serves as the point of entry to the Expense Tracker."""
import sys


def display_menu():
    """Prints menu items to the console."""
    print('\n\t\tExpense Tracker\n')
    print('\t1. Add an expense')
    print('\t2. Print all expenses')
    print('\t3. Exit')


def process_menu_choice():
    """Reads the choice and runs the command."""
    menu_choice = input('\n\tEnter Command Number: ')
    match menu_choice:
        case '1': print('\n\tNot ready yet.')
        case '2': print('\n\tNot ready yet.')
        case '3': sys.exit()
        case _: print(f'\n\t{menu_choice} is not a command.')


def main():
    """Start the Expense Tracker."""
    while True:
        display_menu()
        process_menu_choice()


if __name__ == '__main__':
    main()