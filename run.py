import gspread
from google.oauth2.service_account import Credentials
import math

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("home-expenses-tracker")


def choose_worksheet():
    """
    Allow the user to choose the field to which the expense belongs
    or to access total worksheet.
    Run a while loop to collect a valid string from the user
    via terminal, which must be a string of 1 letter within the possible
    choices. The loop will repeatedly request data until it is valid.
    """
    print("Please select what kind of operation you would like \
to perform:\n-Update a worksheet:\n Please select what \
kind of expense you are updating today:\n 1: Gas bill,\n 2: \
Electricity bill,\n 3: Water bill\
,\n 4: Council tax,\n 5: Phone bill,\n 6: Car expenses,\n 7\
: Food expenses;\n-Set a budget:\n 8: Set a monthly budget\n-View \
totals\n 9: View the totals of your monthly expenses.")
    while True:
        worksheet_choice = input("Input:\n")
        max_num_choices = 9
        if validate_choice(worksheet_choice, max_num_choices):
            break
    return worksheet_choice


def choose_month():
    """
    Allow the user to choose the month to update.
    Run a while loop to collect a valid string of data from the user
    via terminal, which must be a number within 1 and 12.
    The loop will repeatedly request data until it is valid.
    """
    print("Now choose the month for your operation.\
\n1: January,\n2: February,\n3: March,\n\
4: April,\n5: May,\n6: June,\n7: July,\n8: August,\
\n9: September,\n10: October,\n11: November,\
\n12: December\n")
    while True:
        month_choice = input("Input:\n")
        max_num_months = 12

        if validate_choice(month_choice, max_num_months):
            break
    return month_choice


def find_worksheet(chosen_worksheet_num):
    """
    Locate the worksheet that the user has chosen to update
    """
    if chosen_worksheet_num == "6":
        worksheet_name = "car"
    elif chosen_worksheet_num == "7":
        worksheet_name = "food"
    elif chosen_worksheet_num == "8":
        worksheet_name = "budget"
    else:
        worksheet_name = "monthly_bills"
    print(worksheet_name)
    return worksheet_name


def get_expense_data():
    """
    Get expense input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of a number.
    The loop will repeatedly request data until it is valid.
    """
    print("Please enter the value of your expense or \
budget, depending on your previous choice\
\nData should be a decimal or an integer \
number, which will be automatically approximated.\nExample: 109.08\n")
    while True:
        data = input("Enter your data here:\n")
        if validate_input_data(data):
            break
    data_num = math.ceil(float(data))
    return data_num


def update_worksheet(data, chosen_worksheet_num, column, worksheet_name):
    """
    With the data provided, update the relevant cell
    if the first choice was a monthly bill.
    Otherwise, update the first cell available of
    the chosen month column in the relevant worksheet.
    """
    chosen_worksheet = SHEET.worksheet(worksheet_name)
    if int(chosen_worksheet_num) <= 5:
        row = int(chosen_worksheet_num) + 1
        column = int(column) + 1
    else:
        row = len(chosen_worksheet.col_values(column)) + 1
    chosen_worksheet.update_cell(row, column, data)
    month_name = chosen_worksheet.row_values(1)[int(column) - 1]
    print(f"Your {worksheet_name} worksheet has been updated:\n\
The new value for {month_name} is: {data}.\n")


def validate_choice(choice, max_num):
    """
    Inside the try, state that the value must be in a specific range.
    Raise a value error if the string value is not convertible
    into an integer or if it is outside the range.
    """
    try:
        choice_number = int(choice)
        if choice_number < 1 or choice_number > max_num:
            raise ValueError(
                f"Only values between 1 and {max_num} are acceptable, \
you entered: {choice}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_input_data(value):
    """
    Inside the try, convert the string value into an approximated integer.
    Raises ValueError if the string is not convertible into an integer.
    """
    try:
        if float(value) >= 0:
            math.ceil(float(value))
        else:
            raise ValueError(
                "Your value can't be a negative number"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True