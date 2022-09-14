import os
import pycountry
from countryinfo import CountryInfo
import list
import json
from pick import pick
import time
import random


# Splash screen
os.system('cls||clear')
print ('''
 ██████╗ ███████╗ ██████╗ ████████╗██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗ 
██╔════╝ ██╔════╝██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔══██╗
██║  ███╗█████╗  ██║   ██║   ██║   ██████╔╝███████║██║██╔██╗ ██║█████╗  ██████╔╝
██║   ██║██╔══╝  ██║   ██║   ██║   ██╔══██╗██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗ 
╚██████╔╝███████╗╚██████╔╝   ██║   ██║  ██║██║  ██║██║██║ ╚████║███████╗██║  ██║
 ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    ''')

input("\n \t \t \t Press enter to continue")



# Menu selection screen
def menu():
    title = 'Please choose an option and press enter: '
    options = ['Menu1', 'Menu2', 'Menu3']
    option, index = pick(options, title)
    if option == 'Menu1':
        os.system('cls||clear')
        print('You selected Menu1')
    elif option == 'Menu2':
        os.system('cls||clear')
        print('You selected Menu2')
    elif option == 'Menu3':
        os.system('cls||clear')
        print('You selected Menu3')
        exit()


menu()

# title ='Please choose your favorite programming language: '
# options = ['Menu1', 'Menu2', 'Menu3']
# menu_selection, i = pick(options, title)
# print(menu_selection)






# Menu selection
# title = 'Please choose your favorite programming language: '

# choice_1 = ''
# choice_2 = ''
# choice_3 = ''
# choice_4 = ''


# foo = ['a', 'b', 'c', 'd', 'e']
# set={}
# for i in range(4):
#     set.add(random.choice(foo))
#     print(set)
# print(set)

# choices = [choice_1, choice_2, choice_3, choice_4]
# selection, i = pick(choices)
# print(selection)
























