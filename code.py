import asyncio
from colorama import init
import fortnite_api
from fortnite_api import GameLanguage
from termcolor import cprint
from pyfiglet import figlet_format
import os


os.system("title Fortnite Stats")
cprint(figlet_format('Stats', font='big'),
       'blue', attrs=['bold'])

fileName = "key"
print("Add API key in 'key.txt'. Retrieve it at https://www.fortnite-api.com")
file = open(f"{fileName}.txt",encoding='latin-1')
full_text = file.read()
fn = fortnite_api.FortniteAPI(full_text)

def stats(user):
    print("----- Stats for player: "+ user + "-----\n")
    print(fn.stats.fetch_by_name(user))


while True:
    user = input("Player Epic Games Account: ")
    stats(user)
    print("\n")