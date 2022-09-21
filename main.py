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









# def border(func):
#     def inner(arg):
#         print('----------------------------------------------------------------')
#         func(arg)
#         print('----------------------------------------------------------------')
#     return inner


# @border
# def printer(msg):
#     print(msg)








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


























# random_numeric1 = str(random.randint(1, 10))



# print(random_numeric1)
# print(repr(random_numeric1))


# # outputs coutnry name by numeric code
# rand_country1 = pycountry.countries.get(numeric='215')
# print(rand_country1)









# random_country1 = pycountry.countries.get(numeric=12)





# # print(random_country1)










# country= input('Enter a country: ').capitalize()



# # finds capital based on country name
# print (CountryInfo(country).name())





# # print (CountryInfo(country).name())
# # print (CountryInfo(country).capital())





# country_name = input('enter country name: ')
# try:
#     # confirm country is in pycountry database
#     print (pycountry.countries.get(name=country_name).name)
    
    
#     country = CountryInfo(country_name)
#     print(country.capital())





# except:
#     print ('Country not found')













# # help(CountryInfo)

# country = CountryInfo('singapore')
# print(country.info())
# # print(country.all())







# def name_the_captials():
#     pass











# def countries_of_same_letter():
#     # This function will pick a random letter from the alphabet
#     letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
#     country_letter= random.choice(letters)
#     return country_letter



# letter = countries_of_same_letter()
# # # single letter test
# # letter = "Z"

# list_of_countries = []
# number_of_countries = 1
# correct_inputs = []




# country = 'Singapore'

# CountryInfo(country).name()




# # print(country.numeric(0))





















# # Loads list of possible answers to list
# for country in countries:
#     if country.name.startswith(letter):
#         list_of_countries.append(country.name)
#         number_of_countries=len(list_of_countries)
# print(list_of_countries)

# clearing.clear()








































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
    options = ['Menu1', 'Menu2', 'Menu3']
    option, index = pick(options, title)
    if option == 'Menu1':
        clearing.clear()
        print('You selected Menu1\n')
        countries_of_same_letter()
    elif option == 'Menu2':
        clearing.clear()
        print('You selected Menu2')
    elif option == 'Menu3':
        clearing.clear()
        print('You selected Menu3')
        exit()


menu()








# name_countries()
# SystemExit



# clearing.clear()
# lookup()
















# # title ='Please choose your favorite programming language: '
# # options = ['Menu1', 'Menu2', 'Menu3']
# # menu_selection, i = pick(options, title)
# # print(menu_selection)






# # Menu selection
# # title = 'Please choose your favorite programming language: '

# # choice_1 = ''
# # choice_2 = ''
# # choice_3 = ''
# # choice_4 = ''


# # foo = ['a', 'b', 'c', 'd', 'e']
# # set={}
# # for i in range(4):
# #     set.add(random.choice(foo))
# #     print(set)
# # print(set)

# # choices = [choice_1, choice_2, choice_3, choice_4]
# # selection, i = pick(choices)
# # print(selection)
























