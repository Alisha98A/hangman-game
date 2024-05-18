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
SHEET = GSPREAD_CLIENT.open('hangman_game')

scoreboard = SHEET.worksheet('scoreboard')
data = scoreboard.get_all_values()

# List of words
words = """
statement dough blackmail intermediate gallery well reputation resident
operational publisher characteristic bedroom salvation candidate conclusion
knife dash space achievement mastermind copyright dimension onion
possibility proposal guest outside skip crisis astonishing salesperson urgency
lamp replace impact arrogant aunt python proclaim multiply
shareholder mail personality polish cereal storm illusion
""".split()


# Print each word to check if they work
for word in words:
    print(word)