from pycountry import countries
from countryinfo import CountryInfo

import clearing
import random

from colorama import init
from colorama import Fore, Back, Style
from pick import pick
from rand_country import *












def options():

    correct_list=[]
    incorrect_list=[]
    global combined_list
    combined_list=[]


    correct_list=[[0,0,0,'Correct']]
    incorrect_list =[[0,0,0,'Incorrect'],
                    [0,0,0,'Incorrect'],
                    [0,0,0,'Incorrect'],]

    
    correct_list[0][1] = random.choice(rand_country_list())
    correct_list[0][2]= (CountryInfo(correct_list[0][1]).capital())


    for i in range(0,3):
        incorrect_list[i][1] = random.choice(rand_country_list())
        incorrect_list[i-1][2]= (CountryInfo(incorrect_list[i][1]).capital())   
   
    combined_list= correct_list + incorrect_list
    combined_list.sort(key=lambda row: (row[1]))

    combined_list[0][0]='A'
    combined_list[1][0]='B'
    combined_list[2][0]='C'
    combined_list[3][0]='D'






def capitals():
    clearing.clear()


    while True:
        try:
            options()
            break
        except:
            continue

    print(combined_list)
    







    # # option_2 = random.choice(rand_country_list())
    # # option_3 = random.choice(rand_country_list())
    # # option_4 = random.choice(rand_country_list())






    # # print(option_2)
    # # print(option_3)
    # # print(option_4)




    




    # print (CountryInfo(option_1).capital())
    # # print (CountryInfo(option_2).capital())
    # # print (CountryInfo(option_3).capital())
    # # print (CountryInfo(option_4).capital())





    # options =['A', 'B', 'C', 'D']




    # # selection screen

    # # menu['1']="Option 1" 
    # # menu['2']="Option 2"
    # # menu['3']="Option 3"
    # # menu['4']="Exit"








    # # print(f'Select the capital of {country}')
    # # print(f'option 1 {option_1}')






    # # while True: 
    # #     options=menu.keys() 
    # #     for entry in options: 
    # #     print (entry, menu[entry])

    # #     selection=input("Please Select:") 
    # #     if selection =='1': 
    # #     print ("add") 
    # #     elif selection == '2': 
    # #     print ("delete")
    # #     elif selection == '3':
    # #     print ("find") 
    # #     elif selection == '4': 
    # #     break
    # #     else: 
    # #     print ("Unknown Option Selected!")











capitals()