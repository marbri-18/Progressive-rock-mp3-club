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

"""
proto_prog = SHEET.worksheet("Proto-Prog")
beatles = proto_prog.col_values(1)[1:6]
pretty_things = proto_prog.col_values(2)
the_nice = proto_prog.col_values(3)
procol_harum = proto_prog.col_values(4)
moody_blues = proto_prog.col_values(5)
vdgg = proto_prog.col_values(6)
columns = [beatles, pretty_things, the_nice, procol_harum, moody_blues, vdgg ]
pprint(columns)
"""

print("******************************************************************")
print("*            Welcome to the Progressive Rock mp3 club           *")
print("******************************************************************\n \n")

def generate_starting_worksheet_values():
    """
    generates and returns six random numbers in a list.
    returned list to be used for simulated starting accumulated survey values. 
    """
    i = 0
    start_list = []
    while i < 6:
        value = (random.randint(10,30))
        start_list.append(value)
        i += 1
    return (start_list)


def initiate_worksheet(worksheet):
    """
    calls generate_starting_worksheet_values to provide initial 
    simulated data for worksheet.
    appends data row to worksheet specified in arguments.
    """
    data = generate_starting_worksheet_values()
    target_worksheet = SHEET.worksheet(worksheet)
    target_worksheet.append_row(data)




def get_name():
    """
    Gets name input from user
    validates that user has input a name of three characters or more.
    if not valid reports error to use and repeats request.
    if valid welcomes the user and sends request to user to complete survey.
    """
    error = True
    while error:
        name = input("Please enter your first name \n")
        if len(name) < 3:
            print("first name must be 3 characters or more.")
            error = True
        else:
            error = False
    print("\n______________________________________________________________________________________\n")
    print(f"Welcome {name}, \nPlease complete our quick survey")
    print("So we can provide you with recommendations for music you will love")
    print("\n")




def print_instructions():
    """
    Prints welcome and instructions to the user on completing the prog- rock survey
    """
    
    print("In the following 4 questions please rate your favourite bands from top to bottom.")
    print("Give six points to your favourite band in the list, ")
    print("five points for your second favourite and so on ,")
    print("until you get to 1 point for your least favourite band.")
    print("Please note, you must give a different value for each band and you must give a score for every band.")
    print("Your response must be a number - eg/ 1, 2 3, 4, 5, or 6. \n")
    print("\n -------------------------------------------------------\n")

def survey_question(band_name):
    """
    Prints rate band question to user.
    calls check input range and integer function and recieves results.
    if results valid returns user score to get question input function.
    if results not valid repeats question.
    """
    error = True
    while error:
        score = input(f"How many votes do you give for {band_name}?: \n")
        error = check_input_range_and_integer(score)
    return score

def check_input_range_and_integer(num):
    """
    checks user input is integer and between 1 and 6.
    if input not valid prints error message to user and returns error - true to survey question function.
    if input valid returns false to survey question function.
    """
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
    """ 
    checks complete question (genre) data input by user for duplicate values.
    if data valid returns error = false to get get question input function.
    if data not valid prints error message to user and returns error = true to get question input function.
    """

    if len(input) == len(set(input)):
        return False
    else:
        print("Each number entered must be a unique number between 1 and 6. Please try again")
        return True


def get_question_input(qnum, genre, band1, band2, band3, band4, band5, band6):
    """
    Print rate bands list to user.
    call survey questions fuction and recieve back results.
    call check if duplicates function - if results valid return result.
    Otherwise repeat question from beginning.
    """
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

def calculate_total_survey(worksheet, data):
    start_data = SHEET.worksheet(worksheet).get_all_values()
    start_data_row = start_data[-1]
    result_data = []
    for prev, add in zip(start_data_row, data):
        result = int(prev) + int(add)
        result_data.append(result)
    return result_data

def update_worksheet(worksheet, data):
    """
    appends update accumulated data row to worksheet specified in arguments.
    """
    target_worksheet = SHEET.worksheet(worksheet)
    target_worksheet.append_row(data)

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
    highest_value = data.index(max(data))
    worksheet_col = highest_value + 1
    worksheet_row = value = (random.randint(1,5))
    response = []
    target_sheet = SHEET.worksheet(worksheet)
    column = target_sheet.col_values(worksheet_col)
    response.append(column[0])
    response.append(column[worksheet_row])
    return response

def get_band_names(worksheet):
    """ 
    function to get band names from worksheet and return as list.
    """
    band_data = SHEET.worksheet(worksheet).get_all_values()
    band_data_row = band_data[0]
    return band_data_row

def get_accumulated_survey_data(worksheet):
    """
    Called by calculate survey data function.
    gets last row values from worksheet.
    returns values to calculate survey data function.
    """     
    survey_data= SHEET.worksheet(worksheet).get_all_values()
    survey_data_row = survey_data[-1]
    return survey_data_row

def main():
    """
    function to call page functions in correct sequence.
    """
    initiate_worksheet("Proto-Prog")
    initiate_worksheet("Classic-Prog")
    initiate_worksheet("Neo-Prog")
    initiate_worksheet("Contemporary-Prog")
    get_name()
    print_instructions()
    q1_response = get_question_input(1, "Proto-Prog Rock", "The Beatles", "Pink Floyd", "The Pretty Things", "The Nice", "Procol Harum", "The Moody Blues")   
    print(q1_response)
    updated_proto_prog = calculate_total_survey("Proto-Prog", q1_response)
    print(updated_proto_prog)
    update_worksheet("Proto-Prog", updated_proto_prog)
    q1_recommendations = get_user_input_recommendations("Proto-Prog", q1_response)
    print(q1_recommendations)


    q2_response = get_question_input(2, "Classic Prog Rock", "Pink Floyd", "Genesis", "Yes", "Hawkwind", "Rush", "King Crimson")
    print(q2_response)
    updated_classic_prog = calculate_total_survey("Classic-Prog", q2_response)
    print(updated_classic_prog)
    update_worksheet("Classic-Prog", updated_classic_prog)
    q2_recommendations = get_user_input_recommendations("Classic-Prog", q2_response)
    print(q2_recommendations)

    q3_response = get_question_input(3, "Neo-Prog Rock", "Twelfth Night", "Marillion", "IQ", "Pallas", "Pendragon", "Solstice")   
    print(q3_response)
    updated_neo_prog = calculate_total_survey("Neo-Prog", q3_response)
    print(updated_neo_prog)
    update_worksheet("Neo-Prog", updated_neo_prog)
    q3_recommendations = get_user_input_recommendations("Neo-Prog", q3_response)
    print(q3_recommendations)

    q4_response = get_question_input(4, "Contemporary Prog Rock", "Flower Kings", "The Tangent", "Porcupine Tree", "Mostly Autumn", "Dream Theater", "Radiohead")   
    print(q4_response)
    updated_contemporary_prog = calculate_total_survey("Contemporary-Prog", q4_response)
    print(updated_contemporary_prog)
    update_worksheet("Contemporary-Prog", updated_contemporary_prog)
    q4_recommendations = get_user_input_recommendations("Contemporary-Prog", q4_response)
    print(q4_recommendations)

    
main()