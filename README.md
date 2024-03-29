# T1A3 - Terminal Application
# GEO.TRAINER

## Features  

### Name The Countries Mode
This mode is a game that will let user practice their country naming knowledge.   
A randomly selected letter will be displayed and the the user will need to name all the countries beginning with the same letter. The user has 3 chances for any incorrect inputs determined by the list of countries generated.  
**Random Letter and Countries List**  
The random letter and countries list is generated by 2 functions. The first is `rand_letter()` which uses the imported `random.py` module to select a letter from a list of alphabet characters, not including 'x' as there is no countries with names starting with that letter.  
The letter is then passed to another function, `rand_country_list()`, where a for loop compares the first letter of a list of country names inside the imported module `pycountry.py`.    
**User Input Answer**   
The user is prompted to input a country beginning with the same letter displayed. The inputted answer is checked against the generated list, if there is a match a point will be awarded. after the validation the loop begins again until the list of inputted answers is the same length as the generated list of countries.  
**Chance System**  
The game also finishes if the user inputs 3 incorrect answers, that are not on the list. Blank  and mixed case inputs do not count towards an incorrect answer.


### Capitals Mode
This mode is a game to test users knowledge of capital cities. Users will be presented with 4 countries and 4 capital cities, only one pair will be correct, 1 point will be awarded for each correct answer. There are 5 rounds per game.
**Multiple Choice System**  
The country and 

### Lookup Mode
This mode is to allow users to further research information of countries they may have come across while using this app. When the country name is inputted additional information such as the population, currency, calling code, and geographical area.

### Navigation Menu
A navigation menu has been implemented to allow for users to select between the different app modes and also exiting the app.  
The menu accepts up and down cursor buttons and the return button to confirm the selection.  
Any other input will not be registered.

## Testing
The application was tested using a mix of manual testing and a testing script using the pytest module. The aim of the tests was to confirm there would not be any unexpected shutdown of the apps during its operation, interaction between third party modules and user inputs


## How To Install
#### Requirements
Your system will need the latest version of Python,PIP, and Git, before continuing

1. Open Terminal on macOS or Command Prompt on windows
2. Change directory to where you would like to save the application
3. Git clone this repository to your system  
`git clone https://github.com/kenny791/T1A3-Terminal-Application.git`  
6. Install the dependancies  
`sh geotrainer.sh -ir`

#### Running The App
- To run the app after completing the steps above
`sh geotrainer.sh`

#### Help
- For help using the app  
`sh geotrainer.sh -h`

#### Removing Installed Modules 
- Use the code below to remove modules installed by the shell script  
`sh geotrainer.sh -ur`

## Style Guide
This application was written in accordance with Pep8.


## Development Plan
[Trello Board](https://trello.com/b/WhCE9AiQ/t1a3-terminal-application)


## References 
### Installing packages
https://packaging.python.org/en/latest/tutorials/installing-packages/

### Style Guide
https://peps.python.org/pep-0008/

### Ascii title
http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=geo.trainer


### Pycountry
https://pypi.org/project/pycountry/  
https://github.com/flyingcircusio/pycountry  

### Countryinfo
https://pypi.org/project/countryinfo/  
https://github.com/porimol/countryinfo  

### Colorama
https://pypi.org/project/colorama/  
https://github.com/tartley/colorama  

### Clearing
https://pypi.org/project/clearing/  
https://github.com/c00lhawk607/Clearing



## Licence
