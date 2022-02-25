import time
import sys

x = 1

while x == 1:
  char = int(input('''Choose your character
  
  1. Adria
  2. Leon
  3. Harris
  4. Kalen
'''))
  
  
  if char == 1:
    print("Adria Stats:")
    print ("Strengths - Extreme Studying Sweat") # knows lots of things by memory
    print ("Weaknesses - Says MATH") # communication skills are limited
    print ("Special ability - Window Wiping Wave") # defense mechanism
    cont = input('Continue? Y/N')
  
  elif char == 2:
   print('Leon Stats:')
   print ("Strengths - Brain") # can take advantage of situation better
   print ("Weaknesses - Bounces") # less agility
   print ("Special ability - Pickpocketing") # able to steal things with less risk of getting caught
   cont = input('Continue? Y/N')
  
  elif  char == 3:
   print('Harris Stats:')
   print ("Strengths - Plays Two Instruments") #able to confuse zombies with instruments.
   print ("Weaknesses - Wears Tinted Janitor Glasses") # cannot see as well
   print ("Special ability - plays obscure third instrument") # 
   cont = input('Continue? Y/N')
  
  elif char == 4:
    print ("Kalen Stats:")
    print ("Strengths = Head Boy")
    print ("Weaknesses = No PS4")
    print ("Special ability - can take control of situation")
    cont = input('Continue? Y/N')
  if cont == 'Y':
    x = (x+1)
    print("Program will be here")
  elif cont == 'N':
    again = input('OK. Would you like to CHOOSE AGAIN, or EXIT the game?')
