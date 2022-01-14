#A few important basic functions

#import necessary libraries
import os,sys,time,random#, pygame

#basic functions
def screenClear():  #screen clearing function
  # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # for windows platfrom
        _ = os.system('cls')

def pressEnter():  #does a press enter to continue
    input("\n\npress enter to continue")
    screenClear()

def confirm(query="Are you sure? (y or n) "):
    conf = str(input(query))
    if conf == 'y' or conf == 'Y' or conf == 'yes' or conf == 'Yes' or conf == 'YES':
        return True

def slowType(text, delay=0.03): #slowly prints text, and skipps to the end if a key is pressed (so far only ctrl+c). The default delay speed is 0.03, but this can be changed by adding this optionnal parameter. Ex: slowType('text') or slowType('text', 0.1)
    for letter in text:
        try:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        except KeyboardInterrupt: #only works with ctrl+c
            delay = 0


