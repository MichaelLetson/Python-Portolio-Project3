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
    
    return input_data


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


def update_worksheet(data, worksheet):
    """
    Updates worksheet with data input by the user.
    """
    print('Updating worksheet with data provided...')
    updating_worksheet = SHEET.worksheet(worksheet)
    updating_worksheet.append_row(data)
    print(f'{worksheet} worksheet successfully updated!\n')

# def calculate_percentage():
#     """
#     Pulls percentage change data from worksheet and display it to the user.
#     """
#     percentage_data = SHEET.worksheet('PercentageChange').get_all_values()
#     percentage_to_display = percentage_data[-1]
#     print(f'The over all percentage fluctation across all teams is {percentage_to_display}')

def run_program():
    """
    Runs all functions.
    """
    print('Welcome to my Python Project...\n')
    data = collect_data()
    input_data = [int(num) for num in data]
    update_worksheet(input_data, "TeamData")
    calculate_percentage()


run_program()
