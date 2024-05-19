import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import random

# Define the scopes required for accessing Google Sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from a service account file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize the Google Sheets API with the credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the spreadsheet titled 'hangman_game'
SHEET = GSPREAD_CLIENT.open('hangman_game')

# Access the 'scoreboard' worksheet within the spreadsheet
scoreboard = SHEET.worksheet('scoreboard')
data = scoreboard.get_all_values()


# List of words for the hangman game
# The split method was taken from:
# https://www.w3schools.com/python/ref_string_split.asp
words = """
statement dough blackmail intermediate gallery well reputation resident
operational publisher characteristic bedroom salvation candidate conclusion
knife dash space achievement mastermind copyright dimension onion
possibility proposal guest outside skip crisis astonishing salesperson urgency
lamp replace impact arrogant aunt python proclaim multiply
shareholder mail personality polish cereal storm illusion
""".split()


# Function for welcome text using ASCII art generated by 'pyfiglet'
# Code adapted from: https://pypi.org/project/art/
def print_welcome_text():
    text = "Welcome to Hangman Game!"
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)


# Function to print hangman logo
# Code adapted from:
# https://realpython.com/python-main-function/
def print_hangman_logo():
    hangman_logo = """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |
   _|___
  |     |______
  |____________|
    """
    print(hangman_logo)


# Function to print the rules of the game
def print_rules():
    rules = """
    Rules of Hangman:
    1. You need to guess the word letter by letter.
    2. You have a limited number of guesses (6 incorrect guesses).
    3. Each incorrect guess brings the man closer to hanging.
    4. If you guess the word before running out of attempts, you win!
    5. If the man gets hanged, you lose.
    """
    print(rules)


# Function to choose a random word from the list
# Code adapted from:
# https://www.w3schools.com/python/ref_random_choice.asp
def choose_word():
    return random.choice(words).upper()


# Function to display the current state of the word with guessed letters
# https://www.w3schools.com/python/ref_string_join.asp
# https://www.youtube.com/watch?v=N_6YIClAor0
def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {displayed_word}")


# List of hangman drawings for each stage
# Drawings inspired by:
# https://www.youtube.com/watch?v=WV2zPAVRekY
hangman_stages = [
    """
     _______
    |/      |
    |      
    |      
    |       
    |      
    |
   _|___
  |     |______
  |____________|
    """,
    """
     _______
    |/      |
    |      (_)
    |      
    |       
    |      
    |
   _|___
  |     |______
  |____________|
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
   _|___
  |     |______
  |____________|
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|
    |       |
    |      
    |
   _|___
  |     |______
  |____________|
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
   _|___
  |     |______
  |____________|
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
   _|___
  |     |______
  |____________|
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |
   _|___
  |     |______
  |____________|
    """
]

# Function to print the hangman drawing based on remaining attempts
# Code adapted from https://www.youtube.com/watch?v=XwaEo4f17LU
def print_hangman(attempts):
    print(hangman_stages[6 - attempts])

# Main function to run the game
# Code inspired by: https://realpython.com/python-hangman/
def main():
    print_welcome_text()
    print_hangman_logo()
    print_rules()

    start_game = input("Do you want to start the game? (yes/no): ").strip().lower()
    if start_game == 'yes':
        word = choose_word()
        guessed_letters = []
        attempts = 6
        while attempts > 0:
            display_word(word, guessed_letters)
            guess = input("Enter a letter: ").strip().upper()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
                continue
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print(f"Good guess! '{guess}' is in the word.")
            else:
                attempts -= 1
                print(f"Incorrect guess. You have {attempts} attempts left.")
                print_hangman(attempts)
            if all(letter in guessed_letters for letter in word):
                display_word(word, guessed_letters)
                print(f"Congratulations! You guessed the word '{word}'!")
                break
        else:
            print(f"Game over! The word was '{word}'.")
            print_hangman(0)
    else:
        print("Maybe next time!")

if __name__ == "__main__":
    main()
