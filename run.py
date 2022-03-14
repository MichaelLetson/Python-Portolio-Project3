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
    collects data input by the user, and if valid,
    returns confirmation of data.
    """
    while True:
        print('Please enter each teams data from the last calendar')
        print('month, starting with team 1.')
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
    Raising ValueError if values cannot be converted 
    or there are not exactly 5 values.
    """
    try:
        if len(values) != 5:
            raise ValueError('Exactly 5 values are required.')
    except ValueError as error:
        print(f'Invalid entry: {error} - Please try again!')
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Updates worksheet with data input by the user.
    """
    print('Updating worksheet...')
    updating_worksheet = SHEET.worksheet(worksheet)
    updating_worksheet.append_row(data)
    print(f'{worksheet} worksheet successfully updated with new data!\n')


def calculate_percentage():
    """
    Pulls percentage change data from worksheet and display it to the user.
    """
    percentage_data = SHEET.worksheet('PercentageChange').get_all_values()
    percentage_to_display = percentage_data[-2]

    print('The overall percentage fluctation across all')
    print(f'teams is {percentage_to_display}\n')


def get_column_value():
    """
    Gets values from 'SUM' column, ready for calculation for projected data. 
    """
    values_list = SHEET.worksheet('TeamData')

    column_value = []
    column = values_list.col_values(6)
    column_value.append(column[-5:])
    return column_value


def  calculate_projected_data(data):
    """
    Performs calculation for next months projected data.
    """
    print("Calculating next months projected data...")
    new_data = []

    for row in data:
        int_row = [int(num) for num in row]
        average = sum(int_row) / len(int_row)
        new_data.append(round(average))

    update_worksheet(new_data, 'ProjectedData')    

    print(f'Next months projected data for all teams is {new_data}')


def run_program():
    """
    Runs all functions.
    """
    print('Welcome to my Python Project...\n')
    data = collect_data()
    input_data = [int(num) for num in data]
    update_worksheet(input_data, "TeamData")
    calculate_percentage()
    projected_data_to_display = get_column_value()
    calculate_projected_data(projected_data_to_display)
    
run_program()
