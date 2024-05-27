
# The Hangman Game 

![First page](https://github.com/Alisha98A/hangman-game/blob/main/docs/background_feature.png?raw=true)

Visit the deployed application at [Heroku](https://hangman-game-application-b874e04acb8e.herokuapp.com/)

- - -

## CONTENT

* [Testing overview & environment](#testing-overview--environment)
  * [Test environment](#test-environment)
  * [Browser compatibilty](#browser-compatibilty)
* [Automated Testing](#automated-testing)
  * [pep8 validator](https://pep8ci.herokuapp.com/)
* [Manual testing](#manual-testing)
  * [User Stories test](#user-stories-test)
  * [Function Testing](#function-testing)
* [DEFECTS](#defects)
  * [Unsolved issue](#unsolved-issue)
  * [Known issue](#known-issue)

- - -
## Testing overview & environment

Testing was conducted continuously throughout the development phase. Utilizing the CI Python Linter tool and analyzing the terminal output during the build process allowed me to identify and resolve problems promptly. The validation procedure followed the standards set forth in PEP8. Most of the warnings were due to unnecessary or absent whitespace, along with cases of excessive backslashes and inadequate indentation. These concerns have been resolved and corrected.

### Test environment

* Desktop:
  * iMac 21.5
  * MacBook Pro (13-inch, 2017) 
* Screen:
  * Samsung Galaxy S8
  * Iphone 12
  * Iphone 12 Pro


### Browser compatibility

* Google Chrome, version 121.0.6167.86 (Official Build) (64-bit)
* Firefox, version 123.0 (64-bit)


## Automated Testing

No automatic testing apart from using the pep8 validator was performed.

### PEP8 validator 

* [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code.

RESULT: All clear, no errors found

![Pep8 Validation](https://github.com/Alisha98A/hangman-game/blob/main/docs/pep8_validation.png?raw=true)


*<span style="color: blue;">[Back to Content](#content)</span>*

- - -

## Manual test

### User Stories test

`First Time Visitors`

| Goals | Expected Outcome | Testing Performed | Result |
| :--- | :--- | :--- | :--- |
| Learn how to play Hangman | Display a welcome message and instructions on how to play | Verify that the welcome message and instructions are displayed correctly | PASS |
| Confirm interest in game rules | Prompt the player to confirm if they wish to see the game rules before starting | Check that the confirmation prompt appears as expected | PASS |
| Understand game rules | Explain how the game works with clear instructions (1-5) | Ensure that the rules are explained clearly and comprehensively | PASS |

`Returning Visitors`

|  Goals | Expected Outcome | Testing Performed | Result |
| :--- | :--- | :--- | :--- |
| View leaderboard | Display a leaderboard showing top scores and usernames fetched from Google Sheets | Confirm that the leaderboard is displayed accurately and includes the required information | PASS |

`All visitors`
| Goals | Expected Outcome | Testing Performed | Result |
| :--- | :--- | :--- | :--- |
| Guess letters to uncover the hidden word | Allow input of a single letter at a time and provide immediate feedback on its presence in the word | Verify that the application accepts single-letter inputs and provides accurate feedback | PASS |
| Receive immediate feedback on guesses | Inform the player whether the guessed letter is in the word or not, adjusting the number of attempts and displaying the hangman stage accordingly | Test that the application correctly updates the game state based on guesses | PASS |
| Track progress through letter guesses | Reveal the guessed letters in the word, replacing underscores with guessed letters | Confirm that the application displays the current state of the word accurately | PASS |
| Determine win or loss conditions | Announce victory if the word is guessed correctly within the allowed attempts, and announce a loss if all attempts are exhausted without guessing the word | Validate that the application correctly identifies game outcomes | PASS |
| Calculate and view personal score | Compute the score based on the game's difficulty level and offer the option to view and update the global leaderboard | Ensure that the scoring system functions correctly and that the leaderboard functionality is accessible | PASS |
| Compete against self and others | Provide an option to display the global leaderboard and allow adding personal scores to it upon request | Test that the leaderboard is correctly populated and updated with new scores | PASS |
| Allow players to choose between playing another round or viewing the leaderboard. | After each game, the application should prompt the player to choose between playing again or viewing the scoreboard. | Verify that the prompt appears after each game, and both options (play again, view leaderboard) function correctly. | PASS |
| Allow players to enter their names to associate with their scores. | The application should prompt the player to enter their name before finalizing their score. It should validate the name according to predefined criteria (length, alphanumeric characters). | Verify that the name prompt appears before finalizing the score, and the name validation works correctly (length and alphanumeric criteria). | PASS |


*<span style="color: blue;">[Back to Content](#content)</span>*

- - -

### Function Testing

#### Normal Test Case (NRM)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
| NRM-01 | Initialize Google Sheets API| Successful authorization and connection to Google Sheets API | Verified connection with valid credentials | PASS | Successfully connected to Google Sheets API using service account credentials |
| NRM-02 | Load and Access Spreadsheet | Correctly open the 'hangman_game' spreadsheet and access 'scoreboard' worksheet| Verified data retrieval from 'scoreboard' worksheet | PASS| Spreadsheet and worksheet accessed successfully, data retrieved correctly|
| NRM-03 | Clear Terminal | Terminal screen is cleared| Ran clear_terminal function on different OS environments| PASS | Terminal cleared successfully on both Windows and Unix-based systems|
| NRM-04 | Welcome Message Display| Display one of the welcome messages in ASCII art format | Ran print_welcome_text multiple times| PASS | Different welcome messages displayed in ASCII art each time |
| NRM-05 | Hangman Logo Display| Display the hangman logo in ASCII art format| Ran print_hangman_logo function| PASS| Hangman logo displayed correctly|
| NRM-06 | Rules Display | Display game rules in formatted text| Ran print_rules function| PASS | Game rules displayed correctly with proper formatting |
| NRM-07 | Random Word Selection | Randomly select a word from the predefined list | Ran choose_word function multiple times| PASS| Different words selected each time from the list|
| NRM-08 | Display Word State | Show current state of the word with guessed letters | Simulated game with different guessed letters | PASS | Correct word state displayed with guessed letters and underscores|
| NRM-09 |	Hangman Drawing Display | Display the hangman drawing based on remaining attempts |Ran print_hangman with varying attempts | PASS | Correct hangman drawing displayed for each number of attempts left |
| NRM-10 | Input Handling | Correctly handle yes/no input prompts | Tested get_yes_no_input with various inputs | PASS | Function accepted 'yes' or 'no' and prompted again for invalid inputs |
| NRM-11 |Scoreboard Update | Update scoreboard with player's name and score | Simulated game results and updated scoreboard | PASS |	Scoreboard updated correctly, validated top 5 high scores|
| NRM-12 | Show Scoreboard | Display top scores from the Google Sheets 'scoreboard' | Ran show_scoreboard with sample data | PASS | Top scores displayed correctly from the spreadsheet|
| NRM-13 | Play Again or View Scoreboard | Prompt player to choose between playing again or viewing the scoreboard | Tested get_play_scoreboard_input with various inputs| PASS | Function accepted 'play' or 'scoreboard' and prompted again for invalid inputs |
| NRM-14 | 	Name Validation | Validate player's name input| Tested validate_name with various name inputs| PASS | Function correctly validated name length and character constraints |
| NRM-15 | Main Game Flow | Coordinate the full game flow including setup, gameplay, and scoring | Ran main function through several complete game sessions | PASS | Game ran smoothly through multiple sessions, including handling of various inputs and scenarios |


#### Input validation Test (IPU)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
| IPU-01 | 	Name Length Check| Print error message and return False if the name is shorter than 3 characters. | Input name: "Al" | PASS | Error message displayed correctly.|
| IPU-02 | Name Length Check | Print error message and return False if the name is longer than 20 characters | Input name: "A" * 21 | PASS | Error message displayed correctly.|
| IPU-03 | Name Character Check | Print error message and return False if the name contains special characters or spaces. | Input name: "User@123" | PASS | Error message displayed correctly.|
| IPU-04 | 	Name Character Check | Print error message and return False if the name contains only numbers.| Input name: "123456" | PASS | Error message displayed correctly.|
| IPU-05 | Valid Name | Accept the name and return True if it is between 3 and 20 characters long and contains only letters and numbers. | Input name: "Player1" | PASS | 	Name accepted, validation successful. |
| IPU-06 | 	Empty Input Check | Print error message and return False if the input is empty. | Input name: "" | PASS | Error message displayed correctly. |
| IPU-07 | 	Leading/Trailing Spaces | Trim leading and trailing spaces and validate the name. | Input name: " Player1 " | PASS | Leading/trailing spaces trimmed, valid name. |

#### Error Handling (ERR)

| TestCase ID | Feature | Expected Outcome | Testing Performed | Result | Comment |
|---|---|---|---|---|---|
| ERR-01 | Invalid Google Sheets Credentials| Raise an error when invalid credentials are provided  | Modified creds.json with invalid data and attempted connection | PASS | Correctly raised an error for invalid credentials |
| ERR-02 | Google Sheets API Access Denied | Handle access denied error gracefully | Removed necessary permissions from service account and attempted access| PASS | Access denied error handled gracefully, appropriate message displayed |
| ERR-03 | Google Sheets Not Found | Raise an error when the specified spreadsheet is not found| Tried to open a non-existent spreadsheet | PASS | Error raised and handled correctly when spreadsheet was not found |
| ERR-04 | Worksheet Not Found | Raise an error when the specified worksheet is not found | Tried to access a non-existent worksheet| PASS | Error raised and handled correctly when worksheet was not found|
| ERR-05 | Terminal Clear Command Failure | Handle errors during terminal clear command execution | Simulated failure in os.system call | PASS | Error during terminal clear handled gracefully without crashing|
| ERR-06 | Invalid Welcome Message| Handle empty or null welcome messages| Modified welcome_messages list to be empty and ran print_welcome_text | PASS | Handled empty welcome messages list gracefully, displayed fallback message |
| ERR-07 | Invalid Word List | Handle empty or null word list | Modified words list to be empty and ran choose_word | PASS | Handled empty word list gracefully, appropriate message displayed|
| ERR-08 | Invalid Guess Input | Prompt user again on invalid guess input| Entered invalid characters and strings for guess| PASS | 	Invalid guess inputs handled correctly, prompted user again for valid input |
| ERR-09 | 	Network Failure During Score Update | Handle network failure during scoreboard update | Simulated network failure during add_score_to_scoreboard | PASS | Network failure handled gracefully, error message displayed without crashing |
| ERR-10 | Invalid Name Input| Prompt user again on invalid name input | Entered invalid names during validation| PASS | Invalid name inputs handled correctly, prompted user again for valid name|
| ERR-11 | Error Retrieving Scoreboard | Handle errors while retrieving scoreboard data| Simulated errors in show_scoreboard function| PASS | Errors retrieving scoreboard handled gracefully, error message displayed |
| ERR-12 | Invalid Play Again Input | Prompt user again on invalid play again input| Entered invalid options for play again prompt| PASS | Invalid play again inputs handled correctly, prompted user again for valid input |
| ERR-13 | Unexpected Error Handling | General unexpected error handling | Introduced random unexpected errors in the code| PASS | General unexpected errors handled gracefully, error messages displayed without crashing|
