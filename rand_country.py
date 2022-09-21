from pycountry import countries
import clearing
import random
from colorama import init
from colorama import Fore, Back, Style


def rand_letter():
    '''This function will pick a random letter from the alphabet'''
    global country_letter
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
    country_letter = random.choice(letters)
    return country_letter


def rand_country_list():
    '''The function will make a list of countries from a random letter'''
    global list_of_countries
    rand_letter()
    list_of_countries= []

    for country in countries:
        if country.name.startswith(country_letter):
            list_of_countries.append(country.name)
    return list_of_countries

