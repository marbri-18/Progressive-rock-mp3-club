import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("progressive rock mp3 club")


number_list = [33, 37, 25, 21, 23, 25]
def get_user_input_recommendations(worksheet, data):
    """
    Takes worksheet (genre) and data (user responses for each genre) as arguments.
    finds highest value from user responses list.
    from highest value, finds corresponding worksheet column.
    generates random number to determine row to select from column.
    appends heading row value (band name) from selected column to response list.
    appends row value (album title) matching random number from selected column to response list.
    returns response list as recommended album from genre.
    """
    highest_value = number_list.index(max(data))
    worksheet_col = highest_value + 1
    worksheet_row = value = (random.randint(1,5))
    response = []
    target_sheet = SHEET.worksheet(worksheet)
    column = target_sheet.col_values(worksheet_col)
    response.append(column[0])
    response.append(column[worksheet_row])
    return response