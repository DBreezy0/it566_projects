"""Serves as the point of entry to the Diary Application."""
import sys

import diary_entries


def display_menu(diary_file_name):
    """Print the menu and the name of the active diary file."""
    print('\n\t\tDiary Menu\n')
    print(f'\tActive diary file: {diary_file_name}\n')
    print('\t1. Add a diary entry')
    print('\t2. Print all entries')
    print('\t3. Print entries for a date')
    print('\t4. Choose the diary file')
    print('\t5. Load a different diary file')
    print('\t6. Exit')


def print_lines(lines):
    """Print each diary entry. If there are none, print a message."""
    print('')
    if len(lines) == 0:
        print('\tNo entries found.')
    for line in lines:
        print(f'\t{line}', end='')


def add_entry(file_path):
    """Ask for a date and some text then save them as one new line."""
    prompt = '\n\tType the date (mm/dd/yyyy) or press Return for today: '
    entry_date = diary_entries.text_to_date(input(prompt))
    entry_text = input('\tType your diary entry: ')
    diary_entries.save_entry(file_path, entry_date, entry_text)
    print(f'\n\tSaved an entry for {entry_date}.')


def show_all_entries(file_path):
    """Show every entry in the diary file."""
    print_lines(diary_entries.read_lines(file_path))


def show_entries_for_date(file_path):
    """Ask for a date then show only the entries from that date."""
    prompt = '\n\tDate to find (mm/dd/yyyy) or press Return for today: '
    entry_date = diary_entries.text_to_date(input(prompt))
    lines = diary_entries.read_lines(file_path)
    print_lines(diary_entries.find_lines_for_date(lines, entry_date))


def choose_file():
    """Ask for a file name. That file becomes the diary file."""
    new_name = input('\n\tType a diary file name (example: work.txt): ')
    print(f'\n\tThe diary file is now {new_name}.')
    return new_name


def load_file():
    """Ask for the name of a diary file that is already there and load it."""
    new_name = input('\n\tType the name of the diary file to load: ')
    lines = diary_entries.read_lines(diary_entries.get_file_path(new_name))
    print(f'\n\tLoaded {new_name}. It has {len(lines)} lines.')
    return new_name


def main():
    """Keep showing the menu until the user chooses Exit."""
    diary_entries.make_data_folder()
    file_name = diary_entries.DEFAULT_FILE_NAME

    while True:
        display_menu(file_name)
        choice = input('\n\tEnter Command Number: ')
        file_path = diary_entries.get_file_path(file_name)

        try:
            match choice:
                case '1': add_entry(file_path)
                case '2': show_all_entries(file_path)
                case '3': show_entries_for_date(file_path)
                case '4': file_name = choose_file()
                case '5': file_name = load_file()
                case '6':
                    print('\n\tGoodbye!')
                    sys.exit()
                case _: print(f'\n\tWARNING: {choice} is not a command.')
        except Exception as e:
            print(f'\n\tProblem: {e}')


if __name__ == '__main__':
    main()