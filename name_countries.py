from pycountry import countries
import clearing
import random




def letter_picker():
    # This function will pick a random letter from the alphabet
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
    country_letter= random.choice(letters)
    return country_letter



letter = letter_picker()
# # single letter test
# letter = "Z"

list_of_countries = []
number_of_countries = 1
correct_inputs = []





# Loads list of possible answers to list
for country in countries:
    if country.name.startswith(letter):
        list_of_countries.append(country.name)
        number_of_countries=len(list_of_countries)
print(list_of_countries)

clearing.clear()




def name_countries():

    number_of_countries=len(list_of_countries)
    incorrect_input_chances= 3 
    print(f'Name all {number_of_countries} countries that start with the letter {letter}\n')
    while len(list_of_countries) > 0:
        user_input = input(f'Enter a country name starting with {letter}: ').capitalize()
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
                print(f'You got all the countries starting with {letter}!')
                print('You correctly named: ')
                print(*correct_inputs, sep=", ")
                print('\n')
                break
        
        # handles duplicate inputs
        elif user_input in correct_inputs:
            print('You already named that country!')
            print('You correctly named: ')
            print(*correct_inputs, sep=", ")
            print('\u001b[30m\n')

        # handles blank inputs
        elif user_input == '':
            print('You did not enter a country name!')
            print('You correctly named: ')
            print(*correct_inputs, sep=", ")
            print('\n')

        # handles incorrect inputs
        elif user_input not in list_of_countries:
            print(f'Incorrect!, \u001b[31m{user_input}\u001b[30m is not on the list')
            incorrect_input_chances -= 1
            print(f'You have {incorrect_input_chances}/3 chances left\n')
            if incorrect_input_chances == 0:
                clearing.clear()
                print('You have run out of chances!')
                if len(correct_inputs) >0:
                    print('You correctly named: ')
                    print(*correct_inputs, sep=", ")
                    print('\n')
                print('The countries you missed were: ')
                print(*list_of_countries, sep=", ")
                print('\n')
                break

