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











# def border(func):
#     def inner(arg):
#         print('----------------------------------------------------------------')
#         func(arg)
#         print('----------------------------------------------------------------')
#     return inner


# @border
# def printer(msg):
#     print(msg)








def app_controller():
    choice =input('\nPress Enter to search again: \n[m] to go back to menu \n[q] to quit the app\n')

    if choice == 'm':
        pass

    if choice == 'q':
        SystemExit






def lookup():
    clearing.clear()

    searchcountry = input('Please enter country name for more information: ')
    if searchcountry == '':
        lookup()

    country = CountryInfo(searchcountry)

    print(f'Subregion\t{country.subregion()}')
    print(f'Area\t\t{country.area()} sqkm')
    print(f'Population\t{country.population()}')
    print(f'Currency\t{country.currencies()}')
    print(f'Calling Code\t+{country.calling_codes()}')

    app_controller()

    lookup()

    


lookup()



























# def letter_picker():
#     # This function will pick a random letter from the alphabet
#     letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
#     country_letter= random.choice(letters)
#     return country_letter



# letter = letter_picker()
# # # single letter test
# # letter = "Z"

# list_of_countries = []
# number_of_countries = 1
# correct_inputs = []





# # Loads list of possible answers to list
# for country in countries:
#     if country.name.startswith(letter):
#         list_of_countries.append(country.name)
#         number_of_countries=len(list_of_countries)
# print(list_of_countries)

# clearing.clear()








# def name_the_countries():

#     number_of_countries=len(list_of_countries)
#     incorrect_input_chances= 3 
#     print(f'Name all {number_of_countries} countries that start with the letter {letter}\n')
#     while len(list_of_countries) > 0:
#         user_input = input(f'Enter a country name starting with {letter}: ').capitalize()
#         clearing.clear()
        
#         # handles quit command
#         if user_input == 'Q':
#             break
        
#         # handles correct inputs
#         elif user_input in list_of_countries:
#             print('Good Job!')
#             # Removes correct answers from list and adds to correct inputs list
#             list_of_countries.pop(list_of_countries.index(user_input))
#             correct_inputs.append(user_input) 
#             print('You correctly named: ')
#             print(*correct_inputs, sep=", ")
#             print('\n')

#             # handles remaining countries and correct completion
#             if len(list_of_countries) == 0:
#                 clearing.clear()
#                 print(f'You got all the countries starting with {letter}!')
#                 print('You correctly named: ')
#                 print(*correct_inputs, sep=", ")
#                 print('\n')
#                 break
        
#         # handles duplicate inputs
#         elif user_input in correct_inputs:
#             print('You already named that country!')
#             print('You correctly named: ')
#             print(*correct_inputs, sep=", ")
#             print('\u001b[30m\n')

#         # handles blank inputs
#         elif user_input == '':
#             print('You did not enter a country name!')
#             print('You correctly named: ')
#             print(*correct_inputs, sep=", ")
#             print('\n')

#         # handles incorrect inputs
#         elif user_input not in list_of_countries:
#             print(f'Incorrect!, \u001b[31m{user_input}\u001b[30m is not on the list')
#             incorrect_input_chances -= 1
#             print(f'You have {incorrect_input_chances}/3 chances left\n')
#             if incorrect_input_chances == 0:
#                 clearing.clear()
#                 print('You have run out of chances!')
#                 if len(correct_inputs) >0:
#                     print('You correctly named: ')
#                     print(*correct_inputs, sep=", ")
#                     print('\n')
#                 print('The countries you missed were: ')
#                 print(*list_of_countries, sep=", ")
#                 print('\n')
#                 break



# name_the_countries()

# ====================================================================================================




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








































# # Splash screen
# clearing.clear()
# print ('''
#  ██████╗ ███████╗ ██████╗ ████████╗██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗ 
# ██╔════╝ ██╔════╝██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔══██╗
# ██║  ███╗█████╗  ██║   ██║   ██║   ██████╔╝███████║██║██╔██╗ ██║█████╗  ██████╔╝
# ██║   ██║██╔══╝  ██║   ██║   ██║   ██╔══██╗██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗ 
# ╚██████╔╝███████╗╚██████╔╝   ██║   ██║  ██║██║  ██║██║██║ ╚████║███████╗██║  ██║
#  ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
#     ''')

# # input("\n \t \t \t Press enter to continue")
# input()








# # Menu selection screen
# def menu():

#     title = 'Please choose an option and press enter: '
#     options = ['Menu1', 'Menu2', 'Menu3']
#     option, index = pick(options, title)
#     if option == 'Menu1':
#         clearing.clear()
#         print('You selected Menu1\n')
#         countries_of_same_letter()
#     elif option == 'Menu2':
#         clearing.clear()
#         print('You selected Menu2')
#     elif option == 'Menu3':
#         clearing.clear()
#         print('You selected Menu3')
#         exit()


# menu()










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
























