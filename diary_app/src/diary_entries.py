"""Saves and finds diary entries in a text file."""
import os
from datetime import date, datetime

DATA_FOLDER = 'data'
DEFAULT_FILE_NAME = 'diary.txt'
DATE_LENGTH = 10


def make_data_folder():
    """Make the data folder if it is not there yet."""
    folder_path = os.path.join(os.getcwd(), DATA_FOLDER)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def get_file_path(file_name):
    """Give back the full path to a file in the data folder."""
    return os.path.join(os.getcwd(), DATA_FOLDER, file_name)


def file_exists(file_path):
    """Give back True if the file is there or False if it is not."""
    return os.path.exists(file_path)


def text_to_date(date_text):
    """Change text like 10/07/2026 into a date. No text means today."""
    if date_text == '':
        return datetime.now().date()

    date_parts = date_text.split('/')
    if len(date_parts) != 3 or len(date_parts[2]) != 4:
        raise Exception('Please type the date like this: 10/07/2026')

    month = int(date_parts[0])
    day = int(date_parts[1])
    year = int(date_parts[2])
    return date(year=year, month=month, day=day)


def save_entry(file_path, entry_date, entry_text):
    """Add one entry to the end of the file."""
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'{entry_date} {entry_text}\n')


def read_lines(file_path):
    """Read every line in the file and give them back as a list."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def find_lines_for_date(lines, entry_date):
    """Give back only the lines that start with the date."""
    found_lines = []
    for line in lines:
        if line[:DATE_LENGTH] == str(entry_date):
            found_lines.append(line)
    return found_lines