"""
Module to run Prog Rock mp3 Club
"""
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("progressive rock mp3 club")


print("********************************************")
print("* Welcome to the Progressive Rock mp3 club *")
print("********************************************")
print("\n")


def generate_starting_worksheet_values():
    """
    generates and returns six random numbers in a list.
    returned list to be used for simulated starting accumulated
    survey values.
    """
    i = 0
    start_list = []
    while i < 6:
        value = (random.randint(10, 30))
        start_list.append(value)
        i += 1
    return start_list


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
    if valid welcomes the user
    and sends request to user to complete survey.
    """
    error = True
    while error:
        name = input("Please enter your first name \n")
        if len(name) < 3:
            print("first name must be 3 characters or more.")
            error = True
        else:
            error = False

    print(f"Welcome {name}, \nPlease complete our quick survey")
    print("So we can provide you with recommendations")
    print("for music you will love")


def print_instructions():
    """
    Prints welcome and instructions to the user on completing the survey
    """
    print("In the following 4 questions")
    print("please rate your favourite bands from top to bottom.")
    print("Give six points to your favourite band in the list, ")
    print("five points for your second favourite and so on ,")
    print("until you get to 1 point for your least favourite band.")
    print("Please note, you must give a different value for each band")
    print("and you must give a score for every band.")
    print("Your response must be a number - eg/ 1, 2 3, 4, 5, or 6. \n")


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
        print("\n")
        error = check_input_range_and_integer(score)
    return score


def check_input_range_and_integer(num):
    """
    checks user input is integer and between 1 and 6.
    if input not valid prints error message to user and returns error -
    true to survey question function.
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
            print(f"You have entered {num}.")
            print("You must enter either a whole number between 1 and 6")
            return True
    else:
        print("You have not entered a number for this question.")
        print("This question must be answered with a number between 1 and 6.")
        return True


def check_if_duplicates(list_input):
    """
    checks complete question (genre) data input by user for duplicate values.
    if data valid returns error = false to get get question input function.
    if data not valid prints error message to user and returns
    error = true to get question input function.
    """
    if len(list_input) == len(set(list_input)):
        return False
    else:
        print("Each number entered must be a unique number between 1 and 6.")
        print("Please try again")
        return True


def get_question_input(qnum, genre, bands):
    """
    Print rate bands list to user.
    call survey questions fuction and recieve back results.
    call check if duplicates function - if results valid return result.
    Otherwise repeat question from beginning.
    """
    band1, band2, band3, band4, band5, band6 = bands
    error_data = True
    while error_data:
        data = []

        print("")
        print(f"Question {qnum}: {genre}")
        print(f"For the bands in the {genre} category:")
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


def calc_total_survey(worksheet, data):
    """
    gets all data from worksheet survey rows
    adds passed in data from user survey to last data row
    returns result as list
    """
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
    Takes worksheet and data as arguments.
    finds highest value from user responses list.
    from highest value, finds corresponding worksheet column.
    generates random number to determine row to select from column.
    appends heading row value from selected column to response list.
    appends row value matching random number from selected column to response.
    returns response list as recommended album from genre.
    """
    highest_value = data.index(max(data))
    worksheet_col = highest_value + 1
    worksheet_row = (random.randint(1, 5))
    response = []
    target_sheet = SHEET.worksheet(worksheet)
    column = target_sheet.col_values(worksheet_col)
    response.append(column[0])
    response.append(column[worksheet_row])
    return response


def get_band_names(worksheet):
    """
    Function called by compile all bands list function.
    Gets band names from worksheet specified in arguments
    and return as list.
    """
    band_data = SHEET.worksheet(worksheet).get_all_values()
    band_data_row = band_data[0]
    return band_data_row


def get_accumulated_survey_data(worksheet):
    """
    Function called by calculate survey data function.
    gets last row values from worksheet specified in arguments.
    returns values to calculate survey data function.
    """
    survey_data = SHEET.worksheet(worksheet).get_all_values()
    survey_data_row = survey_data[-1]
    return survey_data_row


def compile_all_bands_list():
    """
    Function called by get band of week function.
    Calls get band names function to get list of bands
    in each of the four category questions.
    Compiles single list for all bands from four category lists.
    returns single list to get band of week function.
    """
    band1 = get_band_names("Proto-Prog")
    band2 = get_band_names("Classic-Prog")
    band3 = get_band_names("Neo-Prog")
    band4 = get_band_names("Contemporary-Prog")
    all_bands = band1 + band2 + band3 + band4
    return all_bands


def calculate_survey_data():
    """
    function called by get band of week function.
    Compiles accumulated survey results on last row
    of worksheet for all four category questions and merge into one list.
    Calculates highest value
    returns highest value index to get band of week function.
    """
    survey1 = get_accumulated_survey_data("Proto-Prog")
    survey2 = get_accumulated_survey_data("Classic-Prog")
    survey3 = get_accumulated_survey_data("Neo-Prog")
    survey4 = get_accumulated_survey_data("Contemporary-Prog")
    all_surveys = survey1 + survey2 + survey3 + survey4
    highest_value = all_surveys.index(max(all_surveys))
    return highest_value


def get_band_of_week():
    """
    Calls all bands list function to get a single list of all bands.
    calls calculate survey data function to get highest value index.
    gets band of week from corresponding index in all bands list
    """
    all_bands_list = compile_all_bands_list()
    highest_survey_value_index = calculate_survey_data()
    band_of_week = all_bands_list[highest_survey_value_index]
    return band_of_week


def get_album_of_week_band_index(band_of_week):
    """
    Calls get band names function to get band name lists.
    Checks for band name strings in each list.
    If band name string included in list calls album of week function
    Passing in band name column index and worksheet name as arguments.
    Receives band and album name string data back from band of week function.
    Returns band of week and album of week result

    """
    band1 = get_band_names("Proto-Prog")
    band2 = get_band_names("Classic-Prog")
    band3 = get_band_names("Neo-Prog")
    band4 = get_band_names("Contemporary-Prog")

    if band_of_week in band1:
        band_index = band1.index(band_of_week)
        band_album_offer = get_album_of_week(band_index, "Proto-Prog")
    elif band_of_week in band2:
        band_index = band2.index(band_of_week)
        band_album_offer = get_album_of_week(band_index, "Classic-Prog")
    elif band_of_week in band3:
        band_index = band3.index(band_of_week)
        band_album_offer = get_album_of_week(band_index, "Neo-Prog")
    elif band_of_week in band4:
        band_index = band4.index(band_of_week)
        band_album_offer = get_album_of_week(band_index, "Contemporary-Prog")
    else:
        print("Error: couldn't not find band for album of the week")
    return band_album_offer


def get_album_of_week(band_index, worksheet):
    """
    Called by get album of week band index function.
    Takes worksheet name and band of week column index as arguments.
    Uses arguments and random number generator for row to get
    album in column corresponding to band index.
    returns album value recommendation.
    """
    worksheet_col = band_index + 1
    worksheet_row = (random.randint(1, 5))
    response = []
    target_sheet = SHEET.worksheet(worksheet)
    column = target_sheet.col_values(worksheet_col)
    response.append(column[0])
    response.append(column[worksheet_row])
    return response


def print_recommendations(category, q_rec):
    """
    Prints out album and band reccomendations
    for specified arguments to user.
    """
    q_rec_album = q_rec[1]
    album = q_rec_album.split(":")[0]
    link = q_rec_album.split(": ", 1)[1]
    print("*************************************")
    print("From your responses")
    print(f"in the {category} category")
    print("we recommend")
    print(f"{album}")
    print(f"{link}")
    print(f"by {q_rec[0]}")
    print("*************************************")


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

    q1_bands = ["The Beatles",
                "Pink Floyd",
                "The Pretty Things",
                "The Nice",
                "Procol Harum",
                "The Moody Blues"]
    q1_response = get_question_input(1, "Proto-Prog Rock", q1_bands)
    updated_proto_prog = calc_total_survey("Proto-Prog", q1_response)
    update_worksheet("Proto-Prog", updated_proto_prog)
    q1_rec = get_user_input_recommendations("Proto-Prog", q1_response)
    print_recommendations("Proto-Prog Rock", q1_rec)

    q2_bands = ["Pink Floyd",
                "Genesis",
                "Yes",
                "Hawkwind",
                "Rush",
                "King Crimson"]
    q2_response = get_question_input(2, "Classic Prog Rock", q2_bands)
    updated_classic_prog = calc_total_survey("Classic-Prog", q2_response)
    update_worksheet("Classic-Prog", updated_classic_prog)
    q2_rec = get_user_input_recommendations("Classic-Prog", q2_response)
    print_recommendations("Classic Prog Rock", q2_rec)

    q3_bands = ["Twelfth Night",
                "Marillion",
                "IQ",
                "Pallas",
                "Pendragon",
                "Solstice"]
    q3_response = get_question_input(3, "Neo-Prog Rock", q3_bands)
    updated_neo_prog = calc_total_survey("Neo-Prog", q3_response)
    update_worksheet("Neo-Prog", updated_neo_prog)
    q3_rec = get_user_input_recommendations("Neo-Prog", q3_response)
    print_recommendations("Neo-Prog Rock", q3_rec)

    q4_bands = ["The Flower Kings",
                "The Tangent",
                "Porcupine Tree",
                "Spock's Beard",
                "Dream Theater",
                "Frost*"]
    q4_response = get_question_input(4, "Contemporary Prog Rock", q4_bands)
    updated_cont_prog = calc_total_survey("Contemporary-Prog", q4_response)
    update_worksheet("Contemporary-Prog", updated_cont_prog)
    q4_rec = get_user_input_recommendations("Contemporary-Prog", q4_response)
    print_recommendations("Contemporary Prog Rock", q4_rec)

    band_recommendation = get_band_of_week()
    rec = get_album_of_week_band_index(band_recommendation)

    print("Thank you for completing our survey!\n")
    print("from the responses you have given")
    print("we think the albums you will love are:\n")
    print(f"{q1_rec[1]}")
    print(f"by {q1_rec[0]}")
    print(f"{q2_rec[1]}")
    print(f"by {q2_rec[0]}")
    print(f"{q3_rec[1]}")
    print(f"by {q3_rec[0]}")
    print(f"{q4_rec[1]}")
    print(f"by {q4_rec[0]}")
    print("")
    print("getting album of week ....")
    print("")
    print("Our album of the week on special offer is:\n")
    print(f"{rec[1]}")
    print(f"by {rec[0]}\n \n")
    print("Select 'Run Program' again to repeat survey.")


main()
