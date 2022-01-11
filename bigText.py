from basics import screenClear, pressEnter, confirm, slowType
import colours as c
import chapters as chap
import players as p
from players import save
import time, os, sys, json

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

def bigText(text, color='white', font='larry3d', ):
    cprint(figlet_format(str(text), str(font)),
       str(color))



#cool fonts: isometric1, doh, block, 5lineoblique, starwars, larry3d, smisome1, cybermedium, doom


