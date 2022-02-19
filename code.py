import asyncio
from colorama import init
import fortnite_api
from fortnite_api import GameLanguage
from termcolor import cprint
from pyfiglet import figlet_format
import os

api_key = '380463e95c4f1426977ac7bc1e6f431d4e728f43'

os.system("title Fortnite Stats")
cprint(figlet_format('Stats', font='big'),
       'blue', attrs=['bold'])
fn = fortnite_api.FortniteAPI()
def stats(user):
    print("----- Stats for player: "+ user + "-----\n")
    print(fn.stats.fetch_by_name(user))


while True:
    user = input("Player Epic Games Account: ")
    stats(user)
    
