import os
from re import A
from pycountry import countries
import pycountry
from countryinfo import CountryInfo
import list
import json
from pick import pick
import time
import random










# def border(func):
#     def inner(arg):
#         print('----------------------------------------------------------------')
#         func(arg)
#         print('----------------------------------------------------------------')
#     return inner


# @border
# def printer(msg):
#     print(msg)



def letter_picker():
    # This function will pick a random letter from the alphabet
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
    country_letter= random.choice(letters)
    return country_letter






# letter = letter_picker()
letter = "Z"

list_of_countries = []
number_of_countries = 1
correct_inputs = []





# Loads list of possible answers to list
for country in countries:
    if country.name.startswith(letter):
        list_of_countries.append(country.name)
        number_of_countries=len(list_of_countries)
print(list_of_countries)

os.system('cls||clear')







def name_the_countries():
    incorrect_input_chances= 3 
    print(f'Name all {number_of_countries} countries that start with the letter {letter}\n')
    while len(list_of_countries) > 0:
        user_input = input(f'Enter a country name starting with {letter}: ').capitalize()
        os.system('cls||clear')

        if user_input == 'Q':
            break
            
        elif user_input in list_of_countries:
            print('Good Job!')
            # Removes correct answers from list and adds to correct inputs list
            list_of_countries.pop(list_of_countries.index(user_input))
            correct_inputs.append(user_input) 

            print('You correctly named: ')
            print(*correct_inputs, sep=", ")
            print('\n')

            if len(list_of_countries) == 0:
                os.system('cls||clear')
                print(f'You got all the countries starting with {letter}!')
                print('You correctly named: ')
                print(*correct_inputs, sep=", ")
                print('\n')
                break
        
        elif user_input not in list_of_countries:
            print('Incorrect!')
            incorrect_input_chances -= 1
            print(f'You have {incorrect_input_chances} chances left\n')
            if incorrect_input_chances == 0:
                os.system('cls||clear')
                print('You have run out of chances!')
                if len(correct_inputs) >0:
                    print('You correctly named: ')
                    print(*correct_inputs, sep=", ")
                    print('\n')
                break



name_the_countries()




























    # # print(list_of_countries)
    # print(f'Corrrect answers received: {correct_inputs}')

    # user_input = input('Enter a country name: ').capitalize()

    # if user_input in correct_inputs:
    #     print('You already entered that country!')
    #     user_input = input('Enter a country name: ').capitalize()


# print(f'You got {len(correct_inputs)} correct answers!')

# print('You missed the following countries: ')
# print(*list_of_countries, sep=", ")



























# # Splash screen
# os.system('cls||clear')
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
#         os.system('cls||clear')
#         print('You selected Menu1\n')
#         letter_picker()
#     elif option == 'Menu2':
#         os.system('cls||clear')
#         print('You selected Menu2')
#     elif option == 'Menu3':
#         os.system('cls||clear')
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
























