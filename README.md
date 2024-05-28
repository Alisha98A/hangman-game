# Hangman Game

Immerse yourself in the exciting world of our Hangman game, created just for you thanks to the magic of Python. Imagine sitting at your computer, ready to embark on a journey of mystery and suspense reminiscent of the timeless classic Hangman game, but now brought to life in your own command line interface.

This is not just any game, but a chance for you to exercise your mental muscles by testing your vocabulary and deductive reasoning in a friendly competition. With each guess, you'll either get warmer or colder, getting closer to solving the mystery or facing the dreaded hangman scenario (figuratively speaking, of course).

But why have I developed this game? Well, it's all about making learning fun. I wanted to take the basic building blocks of programming — loops, conditions and string manipulation — and turn them into something truly engaging. It's a testament to how even the simplest ideas can become captivating experiences when combined with creativity and passion.

Whether you're looking for a short break from reality or want to sharpen your cognitive skills, our Hangman game offers both entertainment and educational value. Dive in, have fun, and let's see if you can crack the code before the hangman strikes. I wish you best of luck!

![Mockup Image](https://github.com/Alisha98A/hangman-game/blob/main/docs/mockup.png?raw=true) 

Visit the deployed application at [Heroku](https://hangman-game-application-b874e04acb8e.herokuapp.com/)


---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Flowcharts(#flowcharts)

* [Features](#features)
  * [General Features on Each Page](#general-features)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)


* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Deployment](#local-deployment)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### The Strategy

The primary goal of the Hangman game is to engage users in a challenging yet entertaining activity that tests their vocabulary and problem-solving skills. The game aims to provide a simple, interactive experience that can be enjoyed repeatedly, with the possibility of competing against others through a global leaderboard stored in a Google Sheet. The strategy involves:

- Engagement: Keeping players engaged by providing clear instructions, visual aids (ASCII art), and immediate feedback on their guesses.
- Accessibility: Ensuring the game is accessible to a wide audience by supporting both novice and experienced players through adjustable difficulty levels and hints.
Social Interaction: Incorporating a feature to allow players to compare their scores with others, fostering a sense of competition and community.


### The Scope
The scope includes the following features:

- Gameplay Mechanics: Implementing the core Hangman game mechanics, including guessing letters, updating the game state, and determining win/loss conditions.
- User Interface: Designing a text-based user interface (TUI) that is intuitive and easy to navigate, including displaying the game board, hangman stages, and scoreboards.
- Scoring System: Developing a scoring system that rewards players for correctly guessing words and penalizes them for incorrect guesses, with the option to save high scores to a - Google Sheet.
- Leaderboard Integration: Integrating with Google Sheets to store and display player scores, allowing for competitive play and tracking progress over time.


### The Structure
The application's structure can be divided into several components:

- Initialization: Setting up the game environment, including importing necessary libraries, initializing the Google Sheets API, and preparing the game board and hangman stages.
- Main Game Loop: The core logic of the game, including selecting a random word, handling user guesses, updating the game state, and determining the outcome of the game.
- Input Handling: Functions to manage user inputs, such as validating names, handling guesses, and navigating through the game menu.
- Display Logic: Functions responsible for rendering the game state to the console, including displaying the hangman stages, the current word, and the scoreboard.
- Scoring and Leaderboard: Functions to calculate scores, update the Google Sheet with scores, and display the leaderboard to players.


### The Skeleton
The skeleton of the application outlines the basic framework and flow of the game:
This skeleton provides a high-level overview of how the game flows from initialization to the main game loop, handling user inputs, updating the display, managing scores and leaderboards, and finally finalizing the game upon completion.

---

### User Stories

### User Story for First-Time Players
#### User Story 1: As a first-time player, I want to learn how to play Hangman so that I can participate effectively.
- The application should display a welcome message and instructions on how to play.
- The player should be prompted to confirm if they wish to see the game rules before starting.
- The rules should explain how the game works with clear instructions 1-5


#### User Story 3: As a returning player, I would like to view the leaderboard to see how I rank among the other players.
- The game should display a leaderboard fetched from Google Sheets.
- The leaderboard should show the top scores and usernames.


### User Story for All Players
#### User Story 4: As a player, I want to guess letters to uncover the hidden word so that I can progress in the game.

- The application should allow me to input a single letter at a time.
- It should give me immediate feedback on whether the guessed letter is in the word or not.
- If the letter is incorrect, the application should reduce the number of attempts and display the corresponding hangman stage.

#### User Story 5: As a player, I want to see the current state of the word as I guess letters so that I can track my progress.

- The application should reveal the guessed letters in the word, with underlines replaced by guessed letters.

#### User Story 6: As a player, I want to know when I have won or lost the game so that I can track the result.

- The application should announce victory if I guess the word correctly within the allowed attempts.
- It should announce a loss if I have exhausted all attempts without guessing the word.

#### User Story 7: As a player, I want to see my score and potentially add it to a leaderboard so that I can compete against myself and others.

- The application should calculate my score based on the game's difficulty level.
- It should provide an option to display the global leaderboard stored in Google Sheets.
- Upon my request, my score should be added to the leaderboard.

#### User Story 8: As a player, I want to decide whether to play another round or view the leaderboard so that I can continue engaging with the game.

- After each game, the application should prompt me to choose between playing again or viewing the scoreboard.

#### User Story 9: As a player, I want to enter my name to be associated with my score so that my achievements are recognized.

- The application should prompt me to enter my name before finalizing my score.
- It should validate my name according to predefined criteria (length, alphanumeric characters).

---

## Design

### Colour Scheme

![Color palette](https://github.com/Alisha98A/hangman-game/blob/main/docs/color_palette.png?raw=true)


Colors can increase user experience by providing different colors for different purposes. The Hangman Game employs distinct colors to highlight correct and incorrect guesses which can intuitively communicate progress and prompt users to take necessary actions. Furthermore, using color to denote different game states or outcomes enhances user comprehension and engagement.

### Color Usage in Hangman Game Interface

#### Magenta (shade of pink/purple):
- Purpose: Used for welcome messages and headers.
- Explanation: Magenta is employed to grab users' attention and convey a sense of excitement and warmth as they start or interact with the game. It signifies a welcoming and inviting atmosphere, setting the tone for an enjoyable gaming experience.


#### Yellow:
- Purpose: Hangman logo and certain game messages.
- Explanation: Yellow is utilized to highlight important elements such as the hangman logo and specific game messages. It adds vibrancy and draws attention to key visual elements.

#### Green:
- Purpose: Indicating correct guesses, positive feedback, and successful outcomes.
- Explanation: Green signifies correctness, success, and positivity within the game. It's used to highlight correct guesses, provide positive feedback to the player, and indicate successful completion of the game objectives. Green color is known as something good, and will therefore provide value for the user as something positive.  


#### Red:
- Purpose: Indicating incorrect guesses, warnings, and game over scenarios.
- Explanation: Red is employed to signify errors, warnings, and negative outcomes during gameplay. It's used to highlight incorrect guesses, convey warnings to the player, and indicate unsuccessful attempts or game over scenarios. Red alerts the player to critical information and emphasizes potential risks. Therefore, choosing this color is an excellent choice for these purposes. 

#### Cyan (combination of green and blue color):
- Purpose: Displaying scoreboard entries.
- Explanation: Cyan is used to present scoreboard entries, providing a visually distinct and easily readable format for player names and scores. It enhances the visibility of scoreboard information and ensures clarity in displaying player achievements and rankings. I chose a seperate color for scoreboard entries to recognize it quickly and for enhancing the experience for the user. 


#### Blue:
- Purpose: Displaying player scores.
- Explanation: Blue is employed to present player scores within the game. It provides a clear and contrasting color for displaying numerical values, ensuring that player scores are easily identifiable and distinguishable from other interface elements. Blue is another color I chose to use seperately apart from the other functions due to the same reason as the previous color. 


#### White:
- Purpose: Highlighting interactive prompts and instructions.
- Explanation: White is used to draw attention to interactive prompts, instructions, and questions posed to the player. It serves as a neutral and easily readable color against the black background, ensuring clarity and comprehension of game instructions and queries.


#### Bold Formatting:
- Purpose: Emphasizing important text elements.
- Explanation: Bold formatting is applied to key text elements such as headers, prompts, and feedback messages to emphasize their significance within the interface. It enhances readability and draws attention to critical information, guiding the player through various stages of the game effectively.
  
---

### Typography

I have chosen to include ASCII art for this project and implemented it for the welcome text for different purposes
- Visually appealing: Makes it stand out and is also very user friendly (the text is big and bold which makes it easy to read)
- Customization: Using pyfiglet gives me the freedom to customize the appearence since I can adjust the size, color and font. I specifically used bold and magenta styles in my function because it is suitable for a welcoming text.
- Accessibility: ASCII art is universally accessible across different platforms and devices without the need for special software or hardware. Which ensures that the message will reach a big audience without any problems.
- Cultural Relevance: ASCII art is popular in games which is mainly the purpose of why I implemented it for the welcome text. Since Hangman Game is a game, I used ASCII art to attract users to play. 


![Ascii Art](https://github.com/Alisha98A/hangman-game/blob/main/docs/ascii_art.png?raw=true)

---

### Imagery

I wanted to enhance the user experience by adding a relevant image in the background of the command-line application. 
The image represents a hangman drawing which will make the playing more fun because of all the colors. The image consists of mainly green and brown, green for nature and brown for the hangman structure. Adding this image to the game immediately catches the users attention and connects the users mind to hangman game. 

![Background image](https://github.com/Alisha98A/hangman-game/blob/main/docs/image_backgrund.png?raw=true)

---

### Flowcharts












---

## Features

### Python Imports

#### import gspread and OS
- Used to automate data for the scoreboard hosted on Google Drive. For this project it is specifically used to have a place to score the high scores. Which makes it easy for the user to access the scoreboard from anywhere and anytime. 

#### from google.oauth2.service_account import Credentials
- Used for allowing application to access Google APIs without user interaction. 

#### import pyfiglet
- Used to generate ASCII art from text (welcome text) which improves the layout of the game and makes the text stand out. Enhances the UI experience. 

#### import random
- Used to randomly select word to display in the game, and also to randomly select welcome messages.
For better user experience and variation, I have chosen to randomly select the words that the user has to guess on. This function makes it more fear but also more challenging for the user, since there is no specific order for the words.
Import random is also implemented on the welcome messages, so every time user runs the program it will display randomly selected welcome messages. This is mainly to increase the user experience and make it fun!

#### from rich.console import Console
- Python package for rendering rich text and beautiful formatting. Used to make the content more clear by highlighting what is important and adding colors to different parts of the text. Benefits for the user is that it is very easy to understand. For example by adding red color to incorrect answers, it immediately tells the user that something is wrong. And by adding green color to correct answers, it tells the user that something is good/right since the color is connected to that kind of feeling. Colors can evoke feelings and emotions for the user and since it is a game, using rich package is a good way to make UI experience more appealing.

Each of these imports brings unique capabilities to The Hangman Game, enabling it to work with Google Sheets, authenticate with Google services, generate ASCII art, introduce randomness, enhance console output, and interact with the operating system. 

To install use: ```pip install -name of package-```
To generate a list of installed Python packages use:  ```pip freeze```

---

### General features 

#### Background image
The background image is added to improve the design and layout for the game. 
Since it is a command line application, the image had to be downloaded as an SVG since Heroku does not handle static files. I added a div in the HTML elements and finished with some styling rules to the SVG code, in order for the image to fit on Heroku. Adding a image representing hangman game improves visibility and makes the game more fun and exciting. 
![Background image feature](https://github.com/Alisha98A/hangman-game/blob/main/docs/background_feature.png?raw=true)

#### Words for the game
Words that user gets to guess are already provided as a feature. For their convenience, the words are selected randomly at every game so the user can just sit back, relax and play without having to come up with their own words. 

![Words feature](https://github.com/Alisha98A/hangman-game/blob/main/docs/words_feature.png?raw=true)

#### High Score Table List
I provided this function for the users to make the game competitive and addictive. Having a scoreboard with the top 5 scores globally will give the user a desire to keep playing to get on the scoreboard. Having the ability to add a username on the scoreboard will also increase the user experience since it is something personal, and people tend to like recognition. 

![Scoreboard feature](https://github.com/Alisha98A/hangman-game/blob/main/docs/scoreboard.png?raw=true)

---

### Future Implementations

- In the future I would like to implement degrees of difficulties by either choosing harder words to quess or reducing the chances to win. This feature will attract all kinds of players, both for complete beginners and for people who are ready to challenge themselves more. 

---

### Accessibility
As of now, the Hangman Game application lacks a thorough assessment regarding accessibility features such as compatibility with screen readers, color contrast, and keyboard navigation, which are essential for individuals with disabilities. Acknowledging the significance of inclusivity, I am dedicated to enhancing these areas in forthcoming projects to ensure the application is accessible to everyone. However, I have tried using clear, concise descriptions for menu options and providing feedback in a consistent manner, which support accessibility

*<span style="color: blue;">[Back to Content](#content)</span>*

---

## Technologies Used

* [Visual Studio Code](https://code.visualstudio.com/): A powerful IDE that supports Python development well, offering debugging tools, extensions for Python, and integrated Git control. While Gitpod provides its own web-based VS Code editor, one might use the desktop version for local development or when offline.
* [Code Institute Python Linter](https://pep8ci.herokuapp.com/): A tool to check Python code against some of the style conventions in [PEP8](https://peps.python.org/pep-0008/).
* [Lucid App]([https://lucid.app/](https://lucid.app/documents#/documents?folder_id=recent)): Useful for planning the application's architecture and flowcharts, especially helpful in the design phase to visualize the application flow.
* [Git](https://git-scm.com) used for version control. (```git add```, ```git commit```, ```git push```)
* [GitHub](https://github.com) Essential for version control, allowing you to track changes, collaborate with others (if applicable), and secure online code storage.
* [Heroku](https://www.heroku.com): A platform for deploying and hosting web applications. 
* [Markup Validation Service](https://validator.w3.org/) - Used to check code ensuring that my HTML is error-free and adheres to the latest web standards.
* [PEP8](https://peps.python.org/pep-0008/): Style Guide for Python Code.


---

### Languages Used

I have used [Python](https://www.python.org/) for this project.


*<span style="color: blue;">[Back to Content](#content)</span>*

---

## Functions & Error Handling

### Functions

#### (clear_terminal):
Clears the terminal screen to prepare for new content, improving readability during the game. Used a lot to clear the terminal after user inputs. 

#### (print_welcome_text):
Generates and displays a welcome message using ASCII art created by pyfiglet, enhancing the game's atmosphere.

#### (print_hangman_logo): 
Prints the hangman logo to the console, visually representing the game's theme.

#### (print_rules):
Shows the rules of the hangman game to the user, informing them about how to play.

#### (choose_word): 
Selects a random word from a predefined list for the game.

#### (display_word): 
Reveals the current state of the word, showing guessed letters and underscores for unguessed letters.

#### (hangman_stages):
A list of ASCII art representations of the hangman at different stages of the game, updated based on the number of incorrect guesses.

#### (print_hangman):
Displays the current stage of the hangman based on the number of incorrect guesses.

#### (get_yes_no_input): 
Prompts the user for binary responses (yes/no), validating the input to ensure it matches expected values.

#### (add_score_to_scoreboard):
Updates the Google Sheets scoreboard with the player's name and score, including error handling for potential issues with reading/writing to the sheet.

#### (show_scoreboard): 
Retrieves and displays the top scores from the Google Sheets scoreboard, with error handling for cases where the scoreboard cannot be accessed.

#### (get_play_scoreboard_input): 
Asks the user if they wish to play another round or view the scoreboard, validating the input accordingly.

#### (validate_name):
Ensures the player's name meets certain criteria (length and character type).

### Error Handling

Throughout the code, error handling is implemented primarily through try-except blocks. These blocks catch exceptions that may occur during operations such as interacting with Google Sheets (add_score_to_scoreboard, show_scoreboard) or processing user input (get_yes_no_input, get_play_scoreboard_input). When an exception is caught, an error message is printed to the console, informing the user of the issue.

*<span style="color: blue;">[Back to Content](#content)</span>*

---

## Deployment & Local Development

### Deployment

### Prerequisite


* Confirm that [Python](https://www.python.org/) is set up on your computer.
* Check if Python is installed by looking at its version. You can do this either via a terminal command or by executing a brief snippet of Python code that displays the version details.
* To install packages and modules, opt for pip (for Python 2) or pip3 (for Python 3), based on the version of Python you're using.


### Deploying on Heroku

1. **Heroku Account:**
   - Ensure you have a Heroku account. If you don't, sign up on the Heroku website.
   
2. **GitHub Repository:**
   - Verify that your project is hosted on GitHub.
   
3. **Heroku Dashboard:**
   - Log in to your Heroku account and navigate to the Heroku Dashboard.
   
4. **Create a New App:**
   - On the dashboard, click `New` and choose `Create new app`.
   
5. **App Name:**
   - Pick a unique name for your app.
   
6. **Region & Create App:**
   - Select a region closest to you (EU or USA), then click Create App.
   
7. **New App**
   - From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.   
   
8. **Confidential credentials**
   - If you need to use any private credentials, like CREDS.JSON, add them to the Config Variables section. This step is essential for maintaining the security and integrity of your application, especially when interacting with external services or APIs that require authentication.
   
9. **Add Buildpack**
   - Scroll down the page to the Buildpacks section and select **Add Buildpack**.
   - Ensure the buildpacks are in the correct order: first, select Python, then Node.js. If they are not in this sequence, reorder them by dragging.

10. **Extra files for Heroku deployment**
Heroku requires two additional files for successful deployment:

  - requirements.txt
  - Procfile

     Purpose: These files specify the dependencies to be installed for your application to function correctly.
     Impact on Deployment: Heroku reads this file to understand which packages and versions to install in the deployment environment. 
     Ensures consistency between local and deployed environments, reducing deployment failures and runtime errors.
	  
11. **requirements**
   - To install the requirements for this project (where applicable), use the following command:
     ```pip3 install -r requirements.txt```
	 
12. **Own packages**
   - If you've installed your packages, you need to update the requirements file with:
     ```pip3 freeze --local > requirements.txt```
	 
13. **Procfile**
   - To create the Procfile, use the command below:
     ```echo web: node index.js > Procfile```
	 
14. **Heroku deployment method**
   - Following these steps to connect your frontend terminal and deploy your application to Heroku!


   a. Connect to Heroku:
      Open your Terminal/CLI and log in to Heroku with: ```heroku login -i```
	  
   b. Set Heroku Remote:
      Configure the Heroku remote using: ```heroku git:remote -a app_name``` (substitute app_name with the name of your app)
	  
   c. Git Operations:
      Execute the usual Git commands: ```add```, ```commit```, and ```push``` to update your repository on GitHub.
	  
   d. Deploy to Heroku:
      To deploy, enter: ```git push heroku main``` in the terminal.
	  
   - Alternatively:
You can opt for Automatic Deployment directly from the Heroku app interface.

*<span style="color: blue;">[Back to Content](#content)</span>*   

---

### Local Deployment

The project can be cloned or forked to make a local copy on your system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- ```pip3 install -r requirements.txt```.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, you'll have to manually incorporate these into your new project as well.

*<span style="color: blue;">[Back to Content](#content)</span>*

---

#### How to Fork

Forking the GitHub repository creates a duplicate of the original repository in your own GitHub account. This allows you to explore and modify the content without affecting the original repository. To fork the repository, follow these steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JaqiKal/task-master)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

---

#### How to Clone

To clone the project repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [JaqiKal/task-master](https://github.com/JaqiKal/task-master)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash or Terminal
5. Change the current working directory to the location you want to use for the cloned directory.
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/JaqiKal/task-master`
7. Press Enter to create your local clone.

*<span style="color: blue;">[Back to Content](#content)</span>*

---

## Testing

Please refer to the file [TESTING.md](TESTING.md) for all tests performed.

--- 


## Credits


### Code Used


Integrating Google Sheets API functionalities was a strategic decision aimed at enhancing the game's data management and analytics capabilities. To facilitate this integration, I defined a set of scopes that specify the permissions required for accessing Google Sheets and Google Drive services. These scopes ensure that the application has the necessary access rights to read from and write to spreadsheets and manage files within Google Drive. This code is adapted from Code Institute's Love Sandwiches follow along video.

Here's the adapted code:
![Code used 1](https://github.com/Alisha98A/hangman-game/blob/main/docs/code%20used1.png?raw=true)

--

Incorporating a visually engaging element was essential to enhance player engagement and immersion. One such element is the display of the Hangman logo at the start of the game, which serves as both a visual cue and a part of the game's theme. To achieve this, I adapted a code snippet from a tutorial on Real Python.
The print_hangman_logo function is designed to display the Hangman logo in the terminal. It utilizes a multiline string to define the ASCII art representation of the Hangman figure. This approach allows for easy modification of the logo, which I've made some changes to. 

Here's the adapted code:
![Code used 2](https://github.com/Alisha98A/hangman-game/blob/main/docs/code_used2.png?raw=true)

--
I utilized a crucial piece of functionality that significantly enhances the user experience: clearing the terminal window before displaying new content. This feature ensures that each round of the game starts with a clean slate, providing players with a fresh view of the current state of the game board and other relevant information.

To implement this functionality, I adapted a code snippet from Matt Bodden, who was my mentor at The Code Institute. The function clear_terminal() is designed to execute a system command that clears the terminal window. The choice of command (cls for Windows systems and clear for Unix-based systems) is determined dynamically based on the operating system name, ensuring compatibility across different environments.

Here's the adapted code:
![Code used 3](https://github.com/Alisha98A/hangman-game/blob/main/docs/code_used3.png?raw=true)


---

###  Media

The [background image](https://www.vecteezy.com/vector-art/169193-gallows-illustration) is taken from Vecteezy where I found an image of a hangman drawing with an SVG file, which I downloaded and put into html elements.

---
  
###  Acknowledgments

- I would like to thank [Matt Bodden](https://github.com/MattBCoding) who really took the time to help me! So grateful to have him as my mentor!
- Code Institute Slack Community has been a big support.
- This project was influenced by Love Sandwiches, a code-along project from Code Institute. By trying to understand the underlying principles I have tried to adapt them to my own project. However, this might involve using similar/same intitials and setup.

---

### Content
- [Jenny's Lectures CS IT Youtube video](https://www.youtube.com/watch?v=earqUEBeudg) helped me structure coding with flowcharts for the game
- Love Sandwiches follow along video - for setting up credentials and API for the project
- [W3Schools Split method](https://www.w3schools.com/python/ref_string_split.asp) learned how to use split method for my words list
- ASCII art generated by 'pyfiglet'. Source from: [Pypy](https://pypi.org/project/art/)
- Defining main functions from [Real Python](https://realpython.com/python-main-function/)
- Learned about 'for i in range method' fron [Free code camp](https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/)
- Learned list indexing from [John Watson Rooney's Youtube video](https://www.youtube.com/watch?v=XwaEo4f17LU) 
- Learned how to make the drawing stages from [Catalin tech's youtube video](https://www.youtube.com/watch?v=WV2zPAVRekY)
- Learned about the main game function from [Real Python](https://realpython.com/python-hangman/)
- Hangman drawing adapted from [John Watson Rooney's youtube video](https://www.youtube.com/watch?v=XwaEo4f17LU)
- [W3Schools](https://www.w3schools.com/python/ref_string_join.asp) and [Portfolio Courses youtube video](https://www.youtube.com/watch?v=N_6YIClAor0)  on function to display the current word
- Learned about choosing a random word from [W3Schools](https://www.w3schools.com/python/ref_random_choice.asp) 
- Function to select a random word from the list of words from [W3Schools](https://www.w3schools.com/python/ref_random_choice.asp)
- Function to display the current state of the word with guessed letters [W3Schools](https://www.w3schools.com/python/ref_string_join.asp) and [Portfolio Courses youtube video](https://www.youtube.com/watch?v=N_6YIClAor0)
- Took the color palette generator from [coolors](https://coolors.co/) (for content in README.md file)

---
