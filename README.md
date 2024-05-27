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
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
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

[here](https://github.com/kera-cudmore/Bully-Book-Club#user-experience-ux)

### User Stories

### User Story for First-Time Players
#### User Story 1: As a first-time player, I want to learn how to play Hangman so that I can participate effectively.
- The application should display a welcome message and instructions on how to play.
- The player should be prompted to confirm if they wish to see the game rules before starting.
- The rules should explain how the game works with clear instructions 1-5


### User Story for Returning Players
#### User Story 2: As a returning player, I would like to continue my previous game session so that I can pick up where I left off.
- The game should prompt returning players to enter their username to retrieve their saved game state.
- If a saved game exists, the player should be able to resume their game immediately.

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
  


### Typography

I have chosen to include ASCII art for this project and implemented it for the welcome text for different purposes
- Visually appealing: Makes it stand out and is also very user friendly (the text is big and bold which makes it easy to read)
- Customization: Using pyfiglet gives me the freedom to customize the appearence since I can adjust the size, color and font. I specifically used bold and magenta styles in my function because it is suitable for a welcoming text.
- Accessibility: ASCII art is universally accessible across different platforms and devices without the need for special software or hardware. Which ensures that the message will reach a big audience without any problems.
- Cultural Relevance: ASCII art is popular in games which is mainly the purpose of why I implemented it for the welcome text. Since Hangman Game is a game, I used ASCII art to attract users to play. 


![Ascii Art](https://github.com/Alisha98A/hangman-game/blob/main/docs/ascii_art.png?raw=true)

### Imagery

I wanted to enhance the user experience by adding a relevant image in the background of the command-line application. 
The image represents a hangman drawing which will make the playing more fun because of all the colors. The image consists of mainly green and brown, green for nature and brown for the hangman structure. Adding this image to the game immediately catches the users attention and connects the users mind to hangman game. 

![Background image](https://github.com/Alisha98A/hangman-game/blob/main/docs/image_backgrund.png?raw=true)

### Wireframes

Add the images or links for your wireframes here.

There are lots of different options to create your wireframes - Code Institute students can access [Balsamiq](https://balsamiq.com/) as part of the course.

Some other options include [Figma](https://www.figma.com/), [AdobeXD](https://www.adobe.com/products/xd.html), [Sketch](https://www.sketch.com/?utm_source=google&utm_medium=cpc&adgroup=uxui&device=c&matchtype=e&utm_campaign=ADDICTMOBILE_SKETCH_GAD_DG_UK_T1_ALWAYS-ON_S_TRF_PROS_BRAND&utm_term=sketch&utm_source=google&utm_medium=cpc&utm_content=TOF_BRND__generic&hsa_acc=8710913982&hsa_cam=16831089317&hsa_grp=134620695759&hsa_ad=592060065319&hsa_src=g&hsa_tgt=kwd-14921750&hsa_kw=sketch&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjwr4eYBhDrARIsANPywCjRIFn93DMezYnsyE5Fic_8l8kynJtut0GYMU01TiohHjwziFtlH0gaAhteEALw_wcB) and [Mockup](https://apps.apple.com/us/app/mockup-sketch-ui-ux/id1527554407) to name just a few! Or you can even go old school and get those wireframes completed using pen and paper. Just snap an image of the completed wireframes to add the images to the README.

## Features

👩🏻‍💻 View an example of a completed user experience section [here](https://github.com/kera-cudmore/TheQuizArms#Features)

This section can be used to explain what pages your site is made up of.

### General features on each page

If there is a feature that appears on all pages of your site, include it here. Examples of what to include would the the navigation, a footer and a favicon.

I then like to add a screenshot of each page of the site here, i use [amiresponsive](https://ui.dev/amiresponsive) which allows me to grab an image of the site as it would be displayed on mobile, tablet and desktop, this helps to show the responsiveness of the site.

### Future Implementations

What features would you like to implement in the future on your site? Would you like to add more pages, or create login functionality? Add these plans here.

### Accessibility

Be an amazing developer and get used to thinking about accessibility in all of your projects!

This is the place to make a note of anything you have done with accessibility in mind. Some examples include:

Have you used icons and added aria-labels to enable screen readers to understand these?
Have you ensured your site meets the minimum contrast requirements?
Have you chosen fonts that are dyslexia/accessible friendly?

Code Institute have an amazing channel for all things accessibility (a11y-accessibility) I would highly recommend joining this channel as it contains a wealth of information about accessibility and what we can do as developers to be more inclusive.

## Technologies Used

👩🏻‍💻 View an example of a completed Technologies Used section [here](https://github.com/kera-cudmore/Bully-Book-Club#Technologies-Used)

### Languages Used

Make a note here of all the languages used in creating your project. For the first project this will most likely just be HTML & CSS.

### Frameworks, Libraries & Programs Used

Add any frameworks, libraries or programs used while creating your project.

Make sure to include things like git, GitHub, the program used to make your wireframes, any programs used to compress your images, did you use a CSS framework like Bootstrap? If so add it here (add the version used).

A great tip for this section is to include them as you use them, that way you won't forget what you ended up using when you get to the end of your project.

## Deployment & Local Development

👩🏻‍💻 View an example of a completed Deployment & Local Development section [here](https://github.com/kera-cudmore/TheQuizArms#Deployment)

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

Place instructions on how to fork your project here.

#### How to Clone

Place instructions on how to clone your project here.

## Testing

Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.
  
Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file [here](milestone1-testing.md)

## Credits

👩🏻‍💻 View an example of a completed Credits section [here](https://github.com/kera-cudmore/BookWorm#Credits)

The Credits section is where you can credit all the people and sources you used throughout your project.

### Code Used

If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

### Content

Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

###  Media

If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.
  
###  Acknowledgments

If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.



Credit section
https://www.youtube.com/watch?v=earqUEBeudg helped me structure coding with flowcharts for the game
Love Sandwiches follow along video - for setting up credentials and API for the project
https://www.w3schools.com/python/ref_string_split.asp learned how to use split method for my words list
ASCII art generated by 'pyfiglet'. Source from: https://pypi.org/project/art/
defining main functions https://realpython.com/python-main-function/
https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/ for i in range method
https://www.youtube.com/watch?v=XwaEo4f17LU list indexing
learned how to make the drawing stages https://www.youtube.com/watch?v=WV2zPAVRekY
https://www.vecteezy.com/vector-art/169193-gallows-illustration for the background image



Credit section
https://www.youtube.com/watch?v=earqUEBeudg helped me structure coding with flowcharts for the game
Love Sandwiches follow along video - for setting up credentials and API for the project
https://www.w3schools.com/python/ref_string_split.asp learned how to use split method for my words list
ASCII art generated by 'pyfiglet'. Source from: https://pypi.org/project/art/
defining main functions https://realpython.com/python-main-function/
https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/ for i in range method
https://www.youtube.com/watch?v=XwaEo4f17LU list indexing
learned how to make the drawing stages https://www.youtube.com/watch?v=WV2zPAVRekY
main game function https://realpython.com/python-hangman/
hangman drawing adapted from https://www.youtube.com/watch?v=XwaEo4f17LU
https://www.w3schools.com/python/ref_string_join.asp function to display the current word
#https://www.youtube.com/watch?v=N_6YIClAor0 function to display the current word
https://www.w3schools.com/python/ref_random_choice.asp choose a random word
# Function to select a random word from the list of words
# Code adapted from:https://www.w3schools.com/python/ref_random_choice.asp
# Function to display the current state of the word with guessed letters https://www.w3schools.com/python/ref_string_join.asp and https://www.youtube.com/watch?v=N_6YIClAor0

colour palette from [coolors](https://coolors.co/)


