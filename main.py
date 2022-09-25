from pick import pick
import clearing
import sys, traceback
from colorama import init
from colorama import Fore
from lookup import lookup
from name_countries import name_countries
from capitals import capitals

def selection():
    while True:  
        print('\nPress enter to continue...')
        print('or [m] to go back to the main menu.')
        user_selection=input().upper()  
        print(user_selection)
        if user_selection=='':
            break
        elif user_selection== 'M':
            menu()


# Splash screen
clearing.clear()
print (Fore.BLUE+'''
 ██████  ███████  ██████     ████████ ██████   █████  ██ ███    ██ ███████ ██████  
██       ██      ██    ██       ██    ██   ██ ██   ██ ██ ████   ██ ██      ██   ██ 
██   ███ █████   ██    ██       ██    ██████  ███████ ██ ██ ██  ██ █████   ██████  
██    ██ ██      ██    ██       ██    ██   ██ ██   ██ ██ ██  ██ ██ ██      ██   ██ 
 ██████  ███████  ██████  ██    ██    ██   ██ ██   ██ ██ ██   ████ ███████ ██   ██
    ''')
input("\n \t \t \t Press enter to continue")



# menu screen
def menu():
    '''Menu selection screen'''
    title = 'Please choose an option and press enter: '
    options = ['Name the Countries', 'Learn The Capitals', 'Country Information Lookup','Exit Application']
    option, index  = pick(options, title)
    
    if option == 'Name the Countries':
        clearing.clear()
        print('This option will let you learn about the countries of the world.')
        print('You will need to name all countries starting with a random selected letter.')
        print('You will have 3 chances if you make a mistake.')
        print('Good luck!')
        selection()
        name_countries()
    
    elif option == 'Learn The Capitals':
        clearing.clear()
        print('This option will help you learn the capital cities of the world.')
        print('You will need to select the country that has the correct capital city.')
        print('There will be 5 questions.')
        print('Good luck!')
        selection()
        capitals()

    elif option == 'Country Information Lookup':
        clearing.clear()
        print('This option will help you research more information about countries around the world.')
        selection()

        lookup()
        
    elif option == 'Exit Application':
        clearing.clear()
        sys.exit(0)
menu()