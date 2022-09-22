from pycountry import countries
from countryinfo import CountryInfo
import clearing
import random
from colorama import init
from colorama import Fore
# from pick import pick
from rand_country import *
# import numpy


def menu():
    from main import menu
    menu()



def answers():
    '''This module randomly selects countries and cities and puts them into list '''

    global combined_list
    combined_list=[]
    # defining answer lists, one for the correct answer and a 2d list for the incorrect answers
    correct_list=[[0,0,0,'Correct']]
    incorrect_list =[[0,0,0,'Incorrect'],
                    [0,0,0,'Incorrect'],
                    [0,0,0,'Incorrect'],]

    # randomly selects a country and retrieves the correct captial city
    correct_list[0][1] = random.choice(rand_country_list())
    correct_list[0][2]= (CountryInfo(correct_list[0][1]).capital())

    # assigning the correct city to the wrong country, to produce incorrect answers
    for i in range(0,3):
        incorrect_list[i][1] = random.choice(rand_country_list())
        incorrect_list[i-1][2]= (CountryInfo(incorrect_list[i][1]).capital())   

    # combing and 'shuffling' the answer lists, as answer A would always be correct otherwise
    combined_list= correct_list + incorrect_list
    combined_list.sort(key=lambda row: (row[2]))

    #Assigning each county and city pair a letter for multiple choice
    combined_list[0][0]='A'
    combined_list[1][0]='B'
    combined_list[2][0]='C'
    combined_list[3][0]='D'




def capitals():
    clearing.clear()
    correct = 0
    for question in range(0,5):
        while True:
            try:
                answers()
                break
            except:
                continue

        # print(combined_list)
        

        answer_input =0
        
                
        while True:
            clearing.clear()
            print (f'Question {question+1}/ 5.')
            print(Fore.BLACK+'Select the country with the correct capital city\n')
            print(f'{combined_list[0][0]}. {combined_list[0][1]} - {combined_list[0][2]}')
            print(f'{combined_list[1][0]}. {combined_list[1][1]} - {combined_list[1][2]}')
            print(f'{combined_list[2][0]}. {combined_list[2][1]} - {combined_list[2][2]}')
            print(f'{combined_list[3][0]}. {combined_list[3][1]} - {combined_list[3][2]}')
            answer_input= input('\nInput a,b,c,d for your answer: ').upper()
                
            if answer_input == 'A' or answer_input == 'B' or answer_input == 'C' or answer_input == 'D':
                break
            
        i=0
        while answer_input != combined_list[i][0]:
            i += 1
        if combined_list[i][3] =='Correct':
            print(Fore.GREEN+'You are correct!')
            correct +=1
            while True:
                user_input= input('\nPress enter to continue')
                if user_input == '':
                    break

        else:
            print(Fore.RED+'You are incorrect')
            while True:
                user_input= input('\nPress enter to continue')
                if user_input == '':
                    break


    print(f'\nYou answered: {correct}/5 questions correctly.')
    print(Fore.BLACK+'\nWould you like to play again?')

    while True:
        print('\nPress enter to continue...')
        print('or [m] to go back to the main menu.')
        user_selection=input().upper()  
        print(user_selection)
        if user_selection=='M':
            menu()
        elif user_selection =='':
            break
    capitals() 


    


if __name__ == "__capitals__":
    capitals() 