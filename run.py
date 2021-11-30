import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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



def get_name():
    """
    Gets name input from user
    validates that user has input a name of three characters or more.
    if valid sends request to user to complete survey.
    """
    error = True
    while error:
        name = input("Please enter your first name \n")
        if len(name) < 3:
            print("first name must be 3 characters or more.")
            error = True
        else:
            error = False
    print(f"Welcome {name}, \n Please complete our quick survey")
    print("So we can provide you with recommendations for music you will love")

get_name()

def check_input_range_and_integer(num):
    """
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
    
    """
    if len(input) == len(set(input)):
        return False
    else:
        print("Each number entered must be a unique number between 1 and 6. Please try again")
        return True

def survey_question(band_name):
    error = True
    while error:
        score = input(f"How many votes do you give for {band_name}?: \n")
        error = check_input_range_and_integer(score)
    return score


print("\n")
print("In the following 4 questions please rate your favourite bands from top to bottom.")
print("Give six points to your favourite band in the list, ")
print("five points for your second favourite and so on ,")
print("until you get to 1 point for your least favourite band.")
print("Please note, you must give a different value for each band and you must give a score for every band.")
print("Your response must be a number - eg/ 1, 2 3, 4, 5, or 6. \n")

def get_q1_input():
    """

    """
    q1 = []
    error_q1 = True
    while error_q1:

        print("Question 1: Proto-Prog rock")
        print("For the bands in the Proto-Prog group which comprises of:")
        print("The Beatles")
        print("Pink Floyd \n")
        print("The Pretty Things")
        print("The Nice")
        print("Procol Harum")
        print("The Moody Blues")
        

        
        q1 = []
        score = survey_question("The Beatles")  
        q1.append(score)
        score = survey_question("Pink Floyd")  
        q1.append(score)
        score = survey_question("The Pretty Things")  
        q1.append(score)
        score = survey_question("The Nice")  
        q1.append(score)
        score = survey_question("Procol Harum")  
        q1.append(score)
        score = survey_question("The Moody Blues")  
        q1.append(score)
        

        error_q1 = check_if_duplicates(q1)
    return q1
    
    
    
q1_response = get_q1_input()   
print(q1_response)

    
    
    





def get_q2_input():
    """

    """
    q2 = []
    error_q2 = True
    while error_q2:
        print("Question 2: Classic Prog rock")
        print("For the bands in the Classic-Prog group which comprises of:")
        print("Pink Floyd")
        print("Genesis")
        print("Yes")
        print("Hawkwind")
        print("Rush")
        print("King Crimson \n")
        q2 = []        
        score = survey_question("Pink Floyd")  
        q2.append(score)
        score = survey_question("Genesis")  
        q2.append(score)
        score = survey_question("Yes")  
        q2.append(score)
        score = survey_question("Hawkwind")  
        q2.append(score)
        score = survey_question("Rush")  
        q2.append(score)
        score = survey_question("King Crimson")  
        q2.append(score)


        error_q2 = check_if_duplicates(q2)
    return q2
    
q2_response = get_q2_input()   
print(q2_response)

"""

print("For the bands in the Classic-Prog group which comprises of:")
print("Pink Floyd")
print("Genesis")
print("Yes")
print("Hawkwind")
print("Rush")
print("King Crimson \n")
floyd = input("How many votes do you give for Pink Floyd?: \n")
genesis = input("How many votes do you give for Genesis?: \n")
yes = input("How many votes do you give for Yes?: \n")
hawkwind = input("How many votes do you give for Hawkwind?: \n")
rush = input("How many votes do you give for Rush?: \n")
crimson = input("How many votes do you give for King Crimson?: \n")
print("For the bands in the Neo-Prog group which comprises of:")
print("Twelfth Night")
print("Marillion")
print("IQ")
print("Pallas")
print("Pendragon")
print("Solstice \n")
night = input("How many votes do you give for Twelfth Night?: \n")
marillion = input("How many votes do you give for Marillion?: \n")
iq = input("How many votes do you give for IQ?: \n")
pallas = input("How many votes do you give for Pallas?: \n")
pendragon = input("How many votes do you give for Pendragon?: \n")
solstice = input("How many votes do you give for Solstice?: \n")
print("For the bands in the ontemporary-Prog group which comprises of:")
print("The Flower Kings")
print("The Tangent")
print("Porcupine Tree")
print("Mostly Autumn")
print("Dream Theatre")
print("Radiohead \n")
flower = input("How many votes do you give for The Flower Kings?: \n")
tangent = input("How many votes do you give for the Tangent?: \n")
porcupine = input("How many votes do you give for Porcupine Tree?: \n")
autumn = input("How many votes do you give for Mostly Autumn?: \n")
dream = input("How many votes do you give for Dream Theatre?: \n")
Radiohead = input("How many votes do you give for RadioHead?: \n")
"""