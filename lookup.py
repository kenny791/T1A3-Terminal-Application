from pycountry import countries
import pycountry
from countryinfo import CountryInfo
import clearing
from colorama import init
from colorama import Fore

def menu():
    from main import menu
    menu()


# def search():R
#     user_input =input('test_valid')
#     return user_input

def search():
    try:
        searchcountry = input(Fore.BLUE+'Please enter country name for more information: ')
        if searchcountry == '':
            lookup()


        country = CountryInfo(searchcountry)
        print ('\n')
        print(f'Capital\t\t{country.capital()}')
        print(f'Subregion\t{country.subregion()}')
        print(f'Demonym\t\t{country.demonym()}')
        print(f'Population\t{country.population()}')
        print(f'Area\t\t{country.area()} sqkm')
        print('Currency \t', end="")
        print( *country.currencies(),sep=',')
        print('Time Zone \t', end="")
        print(*country.timezones(),sep=',')
        print('Calling Code \t+', end="")
        print(*country.calling_codes(),sep=',')
        print('\nWould you like to search another country')
    
    except KeyError:

        print('\n')
        print('Country not found, please start a new search and enter another country')





def lookup():
    clearing.clear()
    search()
    
    while True:
        print('\n\nPress enter to continue...')
        print('or [m] to go back to the main menu.')
        user_selection=input().upper()  
        print(user_selection)
        if user_selection=='M':
            menu()
        elif user_selection =='':
            break
    
    lookup()


if __name__ == "__main__":
    lookup()







