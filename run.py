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
