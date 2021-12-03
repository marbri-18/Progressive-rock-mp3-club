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


def survey_question(band_name):
    error = True
    while error:
        score = input(f"How many votes do you give for {band_name}?: \n")
        error = check_input_range_and_integer(score)
    return score

def check_input_range_and_integer(num):
    try:
        int(num)
    except ValueError:
        print("Answer must be a whole number between 1 and 6")
        return True
    if num:
        if int(num) > 0 and int(num) <= 6:
            return False
        else:
            print(f"You have entered {num}. You must enter either a whole number between 1 and 6 for this answer.")
            return True
    else:
        print("You have not entered a number for this question. This question must be answered with a number between 1 and 6.")
        return True

def check_if_duplicates(input):

    if len(input) == len(set(input)):
        return False
    else:
        print("Each number entered must be a unique number between 1 and 6. Please try again")
        return True


def get_question_input(qnum, genre, band1, band2, band3, band4, band5, band6):

    data = []
    error_data = True
    while error_data:

        print(f"Question {qnum}: {genre}")
        print(f"For the bands in the {genre} category which comprises of:")
        print(f"{band1}")
        print(f"{band2}")
        print(f"{band3}")
        print(f"{band4}")
        print(f"{band5}")
        print(f"{band6}")

        score = survey_question(f"{band1}")  
        data.append(score)
        score = survey_question(f"{band2}")  
        data.append(score)
        score = survey_question(f"{band3}")  
        data.append(score)
        score = survey_question(f"{band4}")  
        data.append(score)
        score = survey_question(f"{band5}")  
        data.append(score)
        score = survey_question(f"{band6}")  
        data.append(score)

        error_data = check_if_duplicates(data)
    return data

q1_response = get_question_input(1, "Proto-Prog Rock", "The Beatles", "Pink Floyd", "The Pretty Things", "The Nice", "Procol Harum", "The Moody Blues")   
print(q1_response)
