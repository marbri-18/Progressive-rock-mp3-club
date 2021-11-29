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




print("\n")
print("")
print("In the following 4 questions please rate your favourite bands from top to bottom.")
print("Give six points to your favourite band in the list, ")
print("five points for your second favourite and so on ,")
print("until you get to 1 point for your least favourite band.")
print("Please note, you must give a different value for each band and you must give a score for every band.")
print("Your response must be a number - eg/ 1, 2 3, 4, 5, or 6. \n")
print("Question 1: Proto-Prog rock")
print("For the bands in the Proto-Prog group which comprises of:")
print("The Beatles")
print("The Pretty Things")
print("The Nice")
print("Procol Harum")
print("The Moody Blues")
print("Van Der Graaf Generator \n")
beatles = input("How many votes do you give for the Beatles?: \n")
pretty_things = input("How many votes do you give for the Pretty Things?: \n")
nice = input("How many votes do you give for the Nice?: \n")
procol_harum = input("How many votes do you give for Procol Harum?: \n")
moody = input("How many votes do you give for the Moody Blues?: \n")
graaf = input("How many votes do you give for Van Der Graaf Generator?: \n")
# validate q1 input
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