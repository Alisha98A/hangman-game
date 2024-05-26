import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import random
from rich.console import Console
import os

# Initialize Rich Console
# Ideas taken from:
# https://www.youtube.com/watch?v=4zbehnz-8QU&t=143s
console = Console()

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


# Code adapted from Matt Bodden (mentor at Code Institute)
def clear_terminal():
    """
    Clears the terminal window prior to new content.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Function for welcome text using ASCII art generated by 'pyfiglet'
# Code adapted from: https://pypi.org/project/art/
def print_welcome_text():
    text = "Welcome to Hangman Game!"
    ascii_art = pyfiglet.figlet_format(text)
    console.print(ascii_art, style="bold magenta")


# Function to print hangman logo
# Code adapted from:
# https://realpython.com/python-main-function/
def print_hangman_logo():
    hangman_logo = """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
   _|___
  |     |______
  |____________|
    """
    console.print(hangman_logo, style="bold yellow")


# Function to print the rules of the game
def print_rules():
    rules = """
    [bold]Rules of Hangman:[/bold]
    1. You need to guess the word letter by letter.
    2. You have a limited number of guesses (""" \
    """[bold red]6 incorrect guesses[/bold red]).
    3. Each incorrect guess brings the man closer to hanging.
    4. If you guess the word before running out of attempts, you """ \
    """[bold green]win[/bold green]!
    5. If the man gets hanged, you """ \
    """[bold red]lose[/bold red].
    """
    console.print(rules)


# Function to choose a random word from the list
# Code adapted from:
# https://www.w3schools.com/python/ref_random_choice.asp
def choose_word():
    return random.choice(words).upper()


# Function to display the current state of the word with guessed letters
# https://www.w3schools.com/python/ref_string_join.asp
# https://www.youtube.com/watch?v=N_6YIClAor0
def display_word(word, guessed_letters):
    displayed_word = ''.join([
        letter if letter in guessed_letters else '_'
        for letter in word
    ])
    console.print(f"Word: [bold green]{displayed_word}[/bold green]")


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
    |      \\|
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
    |      \\|/
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
    |      \\|/
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
    |      \\|/
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
    console.print(hangman_stages[6 - attempts], style="bold red")


def add_score_to_scoreboard(name, score):
    """
    Add user name and score to the Google Sheets scoreboard.
    """
    try:
        scoreboard.append_row([name, score])
    except Exception as e:
        console.print(f"[bold red]Error adding score: {e}[/bold red]")


def show_scoreboard():
    console.print("[bold magenta]Scoreboard:[/bold magenta]")
    try:
        headers = scoreboard.row_values(1)
        if 'Name' not in headers or 'Score' not in headers:
            console.print(
                          "[bold red]Headers 'Name' and 'Score'"
                          "not found in the sheet.[/bold red]"
                          )
            return
        records = scoreboard.get_all_records()
        if not records:
            console.print("[bold red]No scores available.[/bold red]")
        else:
            for record in records:
                console.print(
                    f"[bold cyan]{record['Name']}[/bold cyan]: "
                    f"[bold green]{record['Score']}[/bold green]"
                    )

    except Exception as e:
        console.print(f"[bold red]Error retrieving scoreboard: {e}[/bold red]")


# Main function to run the game
# Code inspired by: https://realpython.com/python-hangman/
def main():
    clear_terminal()
    print_welcome_text()

    def get_yes_no_input(prompt):
        while True:
            response = console.input(prompt).strip().lower()
            if response in ['yes', 'no']:
                return response
            console.print("[bold red]Invalid input. "
                          "Please enter 'yes' or 'no'.[/bold red]")
    show_rules = get_yes_no_input("Would you like to see "
                                  "the rules first? (yes/no): ")

    if show_rules == 'yes':
        clear_terminal()
        print_rules()
        print_hangman_logo()

    while True:
        start_game = get_yes_no_input.input(
            "Are you ready to start the game?"
            "(yes/no): ")
        if start_game == 'yes':
            clear_terminal()
            word = choose_word()
            guessed_letters = []
            attempts = 6
        while attempts > 0:
            display_word(word, guessed_letters)
            guess = console.input("Enter a letter: ").strip().upper()

            if not guess.isalpha() or len(guess) != 1:
                console.print(
                    "[bold red]Invalid input. Please enter a single letter."
                    "[/bold red]"
                )
                continue

            if guess in guessed_letters:
                console.print(
                    "[bold yellow]You already guessed that letter."
                    "[/bold yellow]"
                )
            elif guess in word:
                guessed_letters.append(guess)
                console.print(
                    f"[bold green]Good guess! '{guess}' is in the word."
                    "[/bold green]"
                )
            else:
                attempts -= 1
                guessed_letters.append(guess)
                console.print(
                    f"[bold red]Incorrect guess. You have"
                    f" {attempts} attempts left.[/bold red]"
                    )
                print_hangman(attempts)

            if all(letter in guessed_letters for letter in word):
                display_word(word, guessed_letters)
                console.print(
                    f"[bold green]Congratulations!"
                    f"You guessed the word '{word}'!"
                    "[/bold green]"
                )
                break
        else:
            console.print(
                f"[bold red]Game over! The word was '{word}'."
                "[/bold red]"
            )
            print_hangman(0)


if __name__ == "__main__":
    main()
