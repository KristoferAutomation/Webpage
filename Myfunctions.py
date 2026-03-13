'''Local functions'''
import streamlit as st
import os
import sys
import shutil
from datetime import datetime, date, timedelta
import json
import pathlib
import re


def calculate_days_net(invoice_date_str,days:int, only_bussines_days:bool=False):
    """
    Calculate the due date number of days (calendar days or bussines) after the invoice date.
    :param invoice_date_str: Invoice date in 'YYYY-MM-DD' format
    :return: Due date as a string in 'YYYY-MM-DD' format
    """
    if only_bussines_days:
        try:
            invoice_date = datetime.strptime(invoice_date_str, "%Y-%m-%d")
            days_added = 0
            current_date = invoice_date

            while days_added < days:
                current_date += timedelta(days=1)
                if current_date.weekday() < 5:  # Monday=0, Sunday=6
                    days_added += 1

            return current_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    else:
        try:
            invoice_date = datetime.strptime(invoice_date_str, "%Y-%m-%d")
            due_date = invoice_date + timedelta(days=days)
            return due_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")


def is_four_digit_number(num:int) -> bool:
    """
    Checks if the given value is a 4-digit integer (positive or negative).
    """
    # Check if absolute value is between 1000 and 9999
    return 1000 <= abs(num) <= 9999


def get_first_digit(num: int) -> int:
    """
    Returns the first digit of an integer (positive or negative).
    """
    num = abs(num)  # Ignore sign
    while num >= 10:
        num //= 10
    return num


def date_in_range(a:dict,b:dict):
    '''
    Compares two dicts with stringvalues converted to datetime.date elements.
    The input dicts must be: {'start' : start,'stop' : stop}
    '''
    if string_to_date(a['start']) >= string_to_date(b['start']) and string_to_date(a['start']) <= string_to_date(b['stop']) or string_to_date(b['start']) >= string_to_date(a['start']) and string_to_date(b['start']) <= string_to_date(a['stop']):
        return True
    else:
        return False  


def single_date_in_range(date_to_compare:datetime.date,dict_to_campare_with:dict):
    '''
    date_to_compare : datetime.date
    dict_to_campare_with: {'start' : start,'stop' : stop}, values of type str
    '''
    if date_to_compare >= string_to_date(dict_to_campare_with['start']) and date_to_compare <= string_to_date(dict_to_campare_with['stop']):
        return True
    else:
        return False  


def string_to_date(date_str: str, fmt: str = "%Y-%m-%d") -> date:
    """
    Convert a date string to a datetime.date object.
    
    :param date_str: The date string to convert.
    :param fmt: The expected date format (default: YYYY-MM-DD).
    :return: datetime.date object.
    :raises ValueError: If the string does not match the format.
    """
    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string.")
    
    try:
        # Parse string to datetime object
        dt = datetime.strptime(date_str.strip(), fmt)
        return dt.date()
    except ValueError as e:
        raise ValueError(f"Invalid date or format. Expected format: {fmt}") from e


def split_after_x_chars(text:str, x:int, add_dots:bool):
    """
    Splits a string into chunks after every x characters.
    
    Args:
        text (str): The input string.
        x (int): Number of characters per chunk (must be > 0).
    
    Returns:
        The first part of the string.
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")
    if not isinstance(x, int) or x <= 0:
        raise ValueError("Chunk size x must be a positive integer.")

    # Split using slicing in steps of x
    string_list = [text[i:i+x] for i in range(0, len(text), x)]
    shorter_string = string_list[0]

    if len(text) > x and add_dots:
        return shorter_string + "..."
    else:
        return shorter_string


def is_valid_swedish_text(text: str) -> bool:
    """
    Validate that the string:
    - Contains only a-ö, A-Ö, 0-9, spaces, and underscores
    - Has no leading or trailing spaces
    - Allows spaces and underscores only inside the text
    """
    if not isinstance(text, str):
        return False

    # Regex explanation:
    # ^(?! )[A-Za-zÅÄÖåäö0-9_ ]*(?<! )$
    # - ^(?! )   → no leading space
    # - (?<! )$  → no trailing space
    # - [A-Za-zÅÄÖåäö0-9_ ]* → allowed characters
    # - (?!_) and (?<!_) inside pattern to avoid leading/trailing underscores
    pattern = r"^(?![ _])[A-Za-zÅÄÖåäö0-9 _]*(?<![ _])$"

    return bool(re.match(pattern, text))


def convert_float_to_string_with_two_decimals(value:float):
    new_value = format(value, ".2f")
    new_value = new_value.replace(".",",")
    return new_value


def sort_by_after_separator(list_of_strings:list, separator=",",large_to_small:bool=True):
    """
    Sorts a list of strings based on the part after the given separator.
    
    Args:
        data (list[str]): List of strings to sort.
        separator (str): The separator to split on.
    
    Returns:
        list[str]: Sorted list.
    """
    if not isinstance(list_of_strings, list) or not all(isinstance(item, str) for item in list_of_strings):
        raise ValueError("Input must be a list of strings.")

    # Sort using the part after the separator as the key
    return sorted(list_of_strings, key=lambda x: x.split(separator, 1)[1] if separator in x else "",reverse=large_to_small)


def split_string_list(list:list,return_after_separator:bool=True,separator:str=","):
    if return_after_separator is True:
        index = 1
    else:
        index = 0
    return[item.split(separator)[index] for item in list]


def sort_dict_by_keys(dict_to_be_sorted:dict,large_to_small:bool=True):
    return dict(sorted(dict_to_be_sorted.items(), reverse=large_to_small))


def return_everything_befor_sign(text:str,sign:str=','):
    head, sep, tail = text.partition(sign)
    return head


def return_everything_after_sign(text:str,sign:str=','):
    head, sep, tail = text.partition(sign)
    return tail


def repalace_blank_spaces_with_underline(string:str):
    '''Replaces all blank spaces with an underline'''
    return string.replace(" ", "_")


def repalace_underline_with_blank_spaces(string:str):
    '''Replaces all blank spaces with an underline'''
    return string.replace("_", " ")


def save_uploaded_file(path:str,image):
    '''Saves the uploaded file to selected direcory'''
    with open(os.path.join(path,image.name), "wb") as f:
                    f.write(image.getbuffer())
    return image.name


def absolute_path():
    '''Returns the absolute system path to program'''    
    this_path = str(pathlib.Path().absolute())
    return this_path


def load_css(path):
    '''Function to load css from other file'''
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


def todays_date():
    #return str(datetime.now().replace(microsecond=0))
    return str(datetime.now().date())


class DateTimeEncoder(json.JSONEncoder):
    '''Json encoder for datetime objects, returns converted datetime to ISO 8601 string'''
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def write_file(file_content:dict):
    '''creates a json file,
    needs a dict with key of class path from MyStructures   
    '''
    path = file_content['this_path']['full_path']
    with open(path, "w", encoding="utf-8") as f:
        json.dump(file_content, f, cls=DateTimeEncoder, indent=4, ensure_ascii=False)


def read_file_to_dict(path):
    '''Retruns the jason file content as dict'''
    with open(path, 'r', encoding="utf-8") as f:
        json_file = json.load(f) 
    return json_file


def file_exist(path:str):
    '''Checks if a file exists'''
    if os.path.isfile(path):
        return True
    return False


def folder_exists(path:str):
    '''Checks if a folder exist'''
    if os.path.exists(path):
        return True
    return False


def create_folder(path:str):
    '''Creates folder at folder_path if it does not exists'''
    if not folder_exists(path):
        os.makedirs(path)


def move_folder(src, dst):
    """
    Moves a folder and all its contents to a new location.
    If the destination exists, it will be merged or overwritten.
    """
    try:
        # Validate source
        if not os.path.exists(src):
            print(f"Error: Source path '{src}' does not exist.")
            return
                
        if not os.path.isdir(src):
            print(f"Error: '{src}' is not a directory.")
            return
        
        # Ensure destination directory exists
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        # Move folder
        shutil.move(src, dst)


    except PermissionError:
        print("Error: Permission denied. Try running with appropriate privileges.")
    except shutil.Error as e:
        print(f"Shutil error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def move_file(src, dst):
    """
    Moves a file from source_path to destination_path.
    Creates destination directories if they don't exist.
    """
    try:
        # Validate that the source exists and is a file
        if not os.path.isfile(src):
            raise FileNotFoundError(f"Source file not found: {src}")

        # Create destination directory if it doesn't exist
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        # Move the file
        shutil.move(src, dst)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")



def delete_folder(path):
    """
    Deletes a folder and all its contents. 
    """
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return
        if not os.path.isdir(path):
            print(f"Error: '{path}' is not a directory.")
            return
        
        # Remove the directory and all its contents
        shutil.rmtree(path)
    
    except PermissionError:
        print(f"Permission denied: Unable to delete '{path}'. Try running with proper permissions.")
    except OSError as e:
        print(f"Error deleting folder '{path}': {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def delete_file(file_path):
    """
    Deletes a file if it exists.
    :param file_path: Path to the file to delete
    """
    try:
        # Check if file exists
        if os.path.exists(file_path):
            os.remove(file_path)

    except PermissionError:
        print(f"Permission denied: Cannot delete '{file_path}'.")
    except IsADirectoryError:
        print(f"'{file_path}' is a directory, not a file.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")


def rename_file(old_name,new_name):
     os.rename(old_name, new_name)


def copy_file(src_file:str,dest_folder:str):
    shutil.copy2(src_file, dest_folder)


def key_not_exists_case_insensitive(dictionary, key):
    """
    Returns True if the key does NOT exist in the dictionary,
    ignoring case differences.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("First argument must be a dictionary")
    if not isinstance(key, str):
        raise TypeError("Key must be a string")

    # Convert all keys to lowercase for comparison
    lower_keys = {str(k).lower() for k in dictionary.keys()}
    return key.lower() not in lower_keys