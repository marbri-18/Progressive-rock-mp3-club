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


""" def get_last_row(worksheet_name):
  
    survey = SHEET.worksheet(worksheet_name).get_all_values()
    get_survey = survey[-1]
    return get_survey
accum_proto_prog = get_last_row("Proto-Prog")
print(accum_proto_prog)
# TESTED WORKING

q1 = [6, 5, 4, 3, 2, 1]

def add_new_survey(previous, new):
    
    update_output = []
    for accumulated, addition in zip(previous, new):
        output_update = int(accumulated) + int(addition)
        update_output.append(output_update)
    return update_output
new_accum_proto_prog = add_new_survey(accum_proto_prog, q1)
print(new_accum_proto_prog)
#TESTED - WORKING

def update_worksheet(data, worksheet):
    
    target_worksheet = SHEET.worksheet(worksheet)
    target_worksheet.append_row(data)
update_worksheet(new_accum_proto_prog, "Proto-Prog")
#TESTED WORKING """
# 

""" def generate_starting_worksheet_values():
    """
    #generates and returns six random numbers in a list.
    #returned list to be used for simulated starting accumulated survey values. 
    """
    i = 0
    start_list = []
    while i < 6:
        value = (random.randint(10,30))
        start_list.append(value)
        i += 1
    return (start_list)
proto_prog_start_values = generate_starting_worksheet_values()
print(proto_prog_start_values)

def update_worksheet(data, worksheet):
    """
    #appends data row to worksheet specified in arguments.
    """
    target_worksheet = SHEET.worksheet(worksheet)
    target_worksheet.append_row(data)
update_worksheet(proto_prog_start_values, "Proto-Prog")
#TESTED WORKING """

def get_q1_input(num):
question_num = "question" + num
print(question_num)
error_question_num = "error_question_num" + num
print(error_question_num)



question_num = []
error_question_num = True
#while error_question_num:
    #print(error_question_num)

""" print("Question 1: Proto-Prog rock")
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
print("\n -------------------------------------------------------\n")
 """