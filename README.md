
====================================== Game description & rules! =============================

This game is called pig and is played using a 6 faced dice. 
To win a round of this game, one must reach 100 point in total from throwing the dice.
Once it's a players turn to throw the dice, as long as one does not throw a 1 , 
player may continue to throw until they decide to end their round or throws a 1.

If the dice rolls a 1, all points gathered in that same round will be deleted and it's the 
other players turn.
However, if the player choose to end their round , all points gathered in that round will be added to 
a total score for the game.

Gamemodes. 

There are two available options for this game. 
1, One player against the computer, where the player can choose from two 
difficulties on the computer. Once you decide to play against the computer,
there will pop up a selection where you may choose your difficulty to play against.
It is not possible to change difficulty during an ongoing game.

2, player versus player. 
In this gamemode you will play on the same computer
and take turn using the same keyboard for selecting your options.

Cheating. 

there are a dice cheat built in that always will give the highest value possible
from the dice if one should feel the need to use it.

Exit game and ongoing round.

In main menu there will be an option to exit the program
and during an ongoing game there is an option to exit to the main menu. 

========================================================================================================

Project information and structure.

This game was developed as a TDD (test driven development) 
inside the project folder called pycode one can find all the python code files being used,both for the game and tests.
main.py file you can see how the game is structured and go from there. We have kept main as simple as possible by implementing    
gamemode in other classes to easier follow up the different parts. 
gamemodes.py is where the different gamemode can be found if you'd like to see their structure.
dice.py is the object created to play the game and get points. 
bot_levels.py contains the two avaiable bots difficulty. this is basically their "brain" structure.

There is a requirements txt file containing all the software needed to perform tests and run the game. 
In the makefile one can find the structure of how the tests are implmented and how they operate.
Release.md is a text file containing all the different version of the game that has been developt. From here you can see
follow the history of our development of the game. 

========================================================================================================

Installation

OBS! make sure you have make installed on your computer(chocolatey for windows for example)

1. Open terminal Git bash as administrator. 
2. Clone our project.
   command : git clone https://github.com/tobleroo/project-Johias
   Then enter the folder using command : cd project-Johias
3. Run make command : make venv
4. Activate venv using this command : . .venv/Scripts/activate
5. Now install packages by command : make install

6. Now you are all set to go!

========================================================================================================

Play game

1. Start of in Git Bash terminal. 
2. Enter the repository : cd project-Johias
3. activate venv (you can find the command above in installation part).
4. enter pycode folder : cd pycode

5. enter command : python main.py 

Now enjoy the game! 

========================================================================================================

Unittesting.

If one desires to test our program it is available to do so. here is a guide on how. 

1. Open terminal Bash
2. enter project-Johias folder, then enter folder pycode
3. Activate virtual enviroment using this command :  . .venv/Scripts/activate
4. enter command one at a time : 
    - make flake8 (tests the structure of the code)
    - make pylint (also tests the structure of the code)
    - make lint (test both flake8 and pylint at once)
    - make coverage (LÄGG TILL FÖRKLARING)
    - make NÅGOT MER HÄR
5. 

Documentation by docstring guide.

In case you would like to look at the documentation and layout of our program follow these steps. 
1. Enter pycode folder
2. enter : make browserdoc
3. then follow the steps in terminal

If one would like to see the complete pydoc documentation

1. enter : make doc
2. there will be a pydoc folder created in pycode folder containing html files of all classes.


check uml in html

1. 
2. 
3. 
4. 




