from pycountry import countries
import clearing
import random
from colorama import init
from colorama import Fore
from rand_country import *

def menu():
    from main import menu
    menu()


def name_countries():
    '''This is the main body of the function,
    It will prompt the user with a letter
    and the user will need to name all the countries starting with the letter'''
    clearing.clear()
    correct_inputs = []
    number_of_countries = 1
    list_of_countries=rand_country_list()
    country_letter=list_of_countries[0][0]
    number_of_countries=len(list_of_countries)
    incorrect_input_chances= 3 
    print(f'Name all {number_of_countries} countries that start with the letter {country_letter}\n')
    while len(list_of_countries) > 0:
        user_input = input(f'Enter a country name starting with {country_letter}: ').capitalize()
        clearing.clear()
        
        # handles quit command
        if user_input == 'Q':
            break
        
        # handles correct inputs
        elif user_input in list_of_countries:
            print('Good Job!')
            # Removes correct answers from list and adds to correct inputs list
            list_of_countries.pop(list_of_countries.index(user_input))
            correct_inputs.append(user_input) 
            print('You correctly named: ')
            print(*correct_inputs, sep=", ")
            print('\n')

            # handles remaining countries and correct completion
            if len(list_of_countries) == 0:
                clearing.clear()
                print(f'You got all the countries starting with {country_letter}!')
                print('You correctly named: ')
                print(*correct_inputs, sep=", ")
                print('\n')
                break
        
        # handles duplicate inputs
        elif user_input in correct_inputs:
            print('You already named that country!')
            print('You correctly named: ')
            print(*correct_inputs, sep=", ")
            print('\u001b[34m\n')

        # handles blank inputs
        elif user_input == '':
            print('You did not enter a country name!')
            print('You correctly named: ')
            print(*correct_inputs, sep=", ")
            print('\n')

        # handles incorrect inputs
        elif user_input not in list_of_countries:
            print(f'Incorrect!, \u001b[31m{user_input}\u001b[34m is not on the list')
            incorrect_input_chances -= 1
            print(f'You have {incorrect_input_chances}/3 chances left\n')
            if incorrect_input_chances == 0:
                clearing.clear()
                print('You have run out of chances!\n')
                if len(correct_inputs) >0:
                    print('You correctly named: ')
                    print(*correct_inputs, sep=", ")
                    print('\n')
                print('The countries you missed were: ')
                print(*list_of_countries, sep=", ")
                print('\n')
                break
    

    print(Fore.BLUE+'\nWould you like to play again?')

    while True:
        print('\nPress enter to continue...')
        print('or [m] to go back to the main menu.')
        user_selection=input().upper()  
        print(user_selection)
        if user_selection=='M':
            menu()
        elif user_selection =='':
            break
    name_countries() 



if __name__ == "__main__":
    name_countries()