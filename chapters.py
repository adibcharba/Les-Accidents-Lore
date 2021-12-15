import colours as c
from basics import screenClear, pressEnter, confirm, slowType
import time

def c1():
    screenClear()
    c.cyan("Chapter 1: The Birth of a Mistake")
    pressEnter()
    screenClear()
    time.sleep(1)
    slowType("Imagine...\n\n", 0.1)
    time.sleep(1)
    slowType("..a place..\n\n", 0.1)
    time.sleep(1)
    slowType("..where \033[1;31;48mANYTHING\033[1;37;48m can happen.", 0.1)
    time.sleep(2)
    screenClear()
    time.sleep(0.5)
    slowType("Les Accidents Inc. proudly presents:\n\n", 0.1)
    time.sleep(3)
    slowType("LES ACCIDENTS LORE: \033[1;31;48mTHE GAME\033[1;37;48m", 0.1)
    time.sleep(0.5)
    pressEnter()



    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c2()

def c2():
    screenClear()
    c.cyan("Chapter 2: The Attack of the Virus")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c3()

def c3():
    screenClear()
    c.cyan("Chapter 3: Hussein's Trial")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c4()

def c4():
    screenClear()
    c.cyan("Chapter 4: The Civil War")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the next chapter?")
    if confirm() == True:
        c5()

def c5():
    screenClear()
    c.cyan("Chapter 5: Mathieu's ASCENT")
    pressEnter()
    screenClear()

    print("Would you like to preceed to the special issue?")
    if confirm() == True:
        csi()

def csi():
    screenClear()
    c.cyan("Special Issue: Cerial vs Milk")
    pressEnter()
    screenClear()
