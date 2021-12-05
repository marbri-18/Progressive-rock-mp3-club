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


    

    
def get_band_names(worksheet):
    band_data = SHEET.worksheet(worksheet).get_all_values()
    band_data_row = band_data[0]
    return band_data_row
    
def get_accumulated_survey_data(worksheet):    
    survey_data= SHEET.worksheet(worksheet).get_all_values()
    survey_data_row = survey_data[-1]
    return survey_data_row

def calculate_band_of_week():
    band1 = get_band_names("Proto-Prog")
    band2 = get_band_names("Classic-Prog")
    band3 = get_band_names("Neo-Prog")
    band4 = get_band_names("Contemporary-Prog")
    all_bands = band1 + band2 + band3 + band4
    return all_bands


def calculate_survey_data():
    survey1 = get_accumulated_survey_data("Proto-Prog")
    survey2 = get_accumulated_survey_data("Classic-Prog")
    survey3 = get_accumulated_survey_data("Neo-Prog")
    survey4 = get_accumulated_survey_data("Contemporary-Prog")
    all_surveys = survey1 + survey2 + survey3 + survey4
    print(all_surveys)
    highest_value = all_surveys.index(max(all_surveys))
    return highest_value

def get_band_of_week():
    all_bands_list = calculate_band_of_week()
    print(all_bands_list)
    highest_survey_value_index = calculate_survey_data()
    print(highest_survey_value_index)
    band_of_week = all_bands_list[highest_survey_value_index]
    return band_of_week

band_recommendation = get_band_of_week()
print(band_recommendation)

def get_album_of_week_band_index(band_of_week):
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