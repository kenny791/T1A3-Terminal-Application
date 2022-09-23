from pycountry import countries
import pycountry
from countryinfo import CountryInfo
import clearing

def menu():
    from main import menu
    menu()




def lookup():

    clearing.clear()
    try:
        searchcountry = input('Please enter country name for more information: ')
        if searchcountry == '':
            lookup()


        country = CountryInfo(searchcountry)

        print(f'Subregion\t{country.subregion()}')
        print(f'Demonym\t\t{country.demonym()}')
        print(f'Population\t{country.population()}')
        print('Currency \t', end="")
        print( *country.currencies(),sep=',')
        print('Time Zone \t', end="")
        print(*country.timezones(),sep=',')
        print(f'Area\t\t{country.area()} sqkm')
        print('Calling Code \t+', end="")
        print(*country.calling_codes(),sep=',')
        print('\nWould you like to search another country')
    
    except:
        print('\nCountry not found, please enter another country\n')



    while True:
        print('\nPress enter to continue...')
        print('or [m] to go back to the main menu.')
        user_selection=input().upper()  
        print(user_selection)
        if user_selection=='M':
            menu()
        elif user_selection =='':
            break
    
    lookup()


if __name__ == "__lookup__":
    lookup()







