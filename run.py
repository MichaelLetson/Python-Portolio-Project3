import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('team_data')

def collect_data():
    """
    collects data input by the user
    """
    print('Please enter each teams data from the last calendar month, starting with team 1.')
    print("Don't forget to separate each piece of data with a comma.")
    print("For example: 25, 42, 44, 15, 25\n")

    user_data = input('Enter data here: ')
    print(f'Confirmation of data: {user_data}')

collect_data()