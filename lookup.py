from pycountry import countries
import pycountry
from countryinfo import CountryInfo
import clearing



def lookup():
    searchcountry = input('Please enter country name for more information: ')
    if searchcountry == '':
        lookup()


    country = CountryInfo(searchcountry)

    print(f'Region\t\t{country.region()}')
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
