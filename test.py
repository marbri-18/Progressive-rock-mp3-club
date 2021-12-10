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


    

    

    









def get_album_of_week_band_index(band_of_week):
    """
    Calls get band names function to get band name lists.
    Checks for band name strings in each list.
    If band name string included in list calls album of week function 
    Passing in band name column index and worksheet name as arguments.
    Receives band name and album name string data back from band of week function.
    Returns band of week and album of week result

    """
    band1 = get_band_names("Proto-Prog")
    band2 = get_band_names("Classic-Prog")
    band3 = get_band_names("Neo-Prog")
    band4 = get_band_names("Contemporary-Prog")

    if band_of_week in band1:
        band_index = band1.index(band_of_week)
        band_and_album_offer = get_album_of_week(band_index, "Proto-Prog")
    elif band_of_week in band2:
        band_index = band2.index(band_of_week)
        band_and_album_offer = get_album_of_week(band_index, "Classic-Prog")
    elif band_of_week in band3:
        band_index = band3.index(band_of_week)
        band_and_album_offer = get_album_of_week(band_index, "Neo-Prog")
    elif band_of_week in band4:
        band_index = band4.index(band_of_week)
        band_and_album_offer = get_album_of_week(band_index, "Contemporary-Prog")
    else:
        print("Error: couldn't not find band for album of the week")
    return band_and_album_offer



def get_album_of_week(band_index, worksheet):
    worksheet_col = band_index + 1
    worksheet_row = value = (random.randint(1,5))
    response = []
    target_sheet = SHEET.worksheet(worksheet)
    column = target_sheet.col_values(worksheet_col)
    response.append(column[0])
    response.append(column[worksheet_row])
    return response

recommendation = get_album_of_week_band_index(band_recommendation)
print(recommendation)