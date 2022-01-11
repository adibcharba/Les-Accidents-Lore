from basics import screenClear, pressEnter, confirm, slowType
import colours as c
import chapters as chap
import players as p
from players import save
import time, os, sys, json
from bigText import bigText
from playsound import playsound


def music():
  print("music")
  playsound("Funky.wav", False)