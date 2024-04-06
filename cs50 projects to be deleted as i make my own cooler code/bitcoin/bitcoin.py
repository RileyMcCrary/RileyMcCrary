import requests
import json
import sys

try:
    #goes to the website for the price
    web = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    o = web.json()
    #goes into the bpi dictionary to grab USD to grab rate out of the USD dictionary
    index = o['bpi']['USD']['rate_float']
    #multiplies by the number specified for how many bitcoin you'd like
    price = float(sys.argv[1]) * index
    #prints the price with seperator commas
    print('$' + f'{price:,}')

#if the request fails
except requests.RequestException:
    print("There seems to have been an ambiguous error and I'm not going to find out what.....Try again maybe?")
    sys.exit

#if the user does not input an amount in argv
except IndexError:
    print('Missing command-line argument   ')
    sys.exit
#if the input isn't a number
except ValueError:
    print('Command-line argument is not a number')
    sys.exit