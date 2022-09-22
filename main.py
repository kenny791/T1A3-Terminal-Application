# import os
import clearing
# from re import A
# from pycountry import countries
# import pycountry
# from countryinfo import CountryInfo
# import list
# import json
from pick import pick
# import time
# import random
from colorama import init
from colorama import Fore
from lookup import lookup
from name_countries import name_countries
from capitals import capitals



# Splash screen
clearing.clear()
print (Fore.BLUE+'''
 ██████  ███████  ██████     ████████ ██████   █████  ██ ███    ██ ███████ ██████  
██       ██      ██    ██       ██    ██   ██ ██   ██ ██ ████   ██ ██      ██   ██ 
██   ███ █████   ██    ██       ██    ██████  ███████ ██ ██ ██  ██ █████   ██████  
██    ██ ██      ██    ██       ██    ██   ██ ██   ██ ██ ██  ██ ██ ██      ██   ██ 
 ██████  ███████  ██████  ██    ██    ██   ██ ██   ██ ██ ██   ████ ███████ ██   ██
    ''')
input("\n \t \t \t\t Press enter to continue")




def menu():
    '''Menu selection screen'''
    title = 'Please choose an option and press enter: '
    options = ['Name the Countries', 'Learn the capitals', 'Exit']
    option, index = pick(options, title)
    if option == 'Name the Countries':


        name_countries()

        SystemExit
    elif option == 'Learn the capitals':
        capitals()

    elif option == 'Country Information Lookup':
        lookup()
        clearing.clear()
        lookup()
    elif option == 'Exit':
        clearing.clear()
        exit()
        SystemExit


menu()
