# import os
import clearing
# from re import A
from pycountry import countries
import pycountry
from countryinfo import CountryInfo
import list
import json
from pick import pick
import time
import random
from colorama import init
from colorama import Fore, Back, Style
from lookup import lookup

from name_countries import name_countries




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



# Menu selection screen
def menu():
    title = 'Please choose an option and press enter: '
    options = ['Name the Countries', 'Menu2', 'Exit']
    option, index = pick(options, title)
    if option == 'Name the Countries':
        clearing.clear()
        print(Fore.BLACK+''' ---NAME THE COUNTRIES---
    Welcome to the Name the countries training module. 
    Here you can test your skills by naming all the countries starting with the letter prompted. You will have 3 chances for any mistakes. Have fun!
        ''')
        input("Press enter to continue")
        clearing.clear()

        name_countries()
        exit()
        SystemExit
    elif option == 'Menu2':
        pass

    elif option == 'Country Information Lookup':
        clearing.clear()
        lookup()
    elif option == 'Exit':
        clearing.clear()
        exit()
        SystemExit


menu()









# def app_controller():
#     choice =input('\nPress Enter to search again: \n[m] to go back to menu \n[q] to quit the app\n')

#     if choice == 'm':
#         pass

#     if choice == 'q':
#         SystemExit









# # selection screen

# menu = {}
# menu['1']="Option 1" 
# menu['2']="Option 2"
# menu['3']="Option 3"
# menu['4']="Exit"







# while True: 
#     options=menu.keys() 
#     for entry in options: 
#       print (entry, menu[entry])

#     selection=input("Please Select:") 
#     if selection =='1': 
#       print ("add") 
#     elif selection == '2': 
#       print ("delete")
#     elif selection == '3':
#       print ("find") 
#     elif selection == '4': 
#       break
#     else: 
#       print ("Unknown Option Selected!")









