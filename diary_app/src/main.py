"""Serves as the point of entry to the Diary Application."""


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


def main():
    """Run the Diary Application."""
    diary_file_name = 'diary.txt'
    display_menu(diary_file_name)


if __name__ == '__main__':
    main()