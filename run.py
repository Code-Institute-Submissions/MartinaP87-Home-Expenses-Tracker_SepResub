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