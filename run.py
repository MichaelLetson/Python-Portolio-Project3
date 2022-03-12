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
    collects data input by the user, and if valid, returns confirmation of data. 
    """
    while True:
        print('Please enter each teams data from the last calendar month, starting with team 1.')
        print("Don't forget to separate each piece of data with a comma.")
        print("For example: 25,42,44,15,25\n")

        user_data = input('Enter data here: ')
        input_data = user_data.split(',')
    
        if validate_data(input_data):
            print(f'Confirmation of data: {input_data}')
            break

def validate_data(values):
    """
    Converts values into integers. 
    Raising ValueError if values cannot be converted or there are not exactly 5 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f'Exactly 5 values are required.'
            )
    except ValueError as error:
        print(f'Invalid entry: {error} - Please try again!')
        return False
    
    return True

collect_data()