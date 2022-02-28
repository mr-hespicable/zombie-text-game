import time, random, sys, os
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
    cont = input('Continue? Y/N \n')
  
  elif char == 2:
   print('Leon Stats:')
   print ("Strengths - Brain") # can take advantage of situation better
   print ("Weaknesses - Bounces") # less agility
   print ("Special ability - Pickpocketing") # able to steal things with less risk of getting caught
   cont = input('Continue? Y/N \n')
  
  elif  char == 3:
   print('Harris Stats:')
   print ("Strengths - Plays Two Instruments") #able to confuse zombies with instruments.
   print ("Weaknesses - Wears Tinted Janitor Glasses") # cannot see as well
   print ("Special ability - Plays Obscure Third Instrument") # will come in handy later
   cont = input('Continue? Y/N \n')
  
  elif char == 4:
    print ("Kalen Stats:")
    print ("Strengths = Head Boy") # leadership role
    print ("Weaknesses = No PS4") # bad reaction time
    print ("Special ability - Emotional Damage") # EMOTIONAL DAMAGE
    cont = input('Continue? Y/N \n')
  if cont == 'Y':
    x = (x+1)
    message1 = 'DECEMBER 14 2048\n'
    for char in message1: # typewriter effect, very cool. took a really long time to figure out, had to watch several youtube videos explaining how sys works. i still don't get it fully.
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.001) #0.08
    
    time.sleep(2)

    message2 = '\nA zombie apocalypse has broken out in England. You must reach the signal tower emitting the dangerous spores that are infecting the public.\nUnfortunately, the signal tower is located in the IKEA warehouse full of English zombies yelling ' '"Bloody foreigners!"' ' Sadly, you are not from England, so you are at great risk to these zombies. You will have to make different choices that affect the story, with many resulting in death.\n'
    for char in message2: 
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.001) #0.03

    time.sleep(1)
    message3 = "Welcome to the Apocolypse.\n"
    for char in message3: 
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.001) #0.2

    def zombieAttributes(self):
      
      zombieHealth = random.randint(20,30)
      

    class action:
      def shovelAction(self):
        if item == 'shovel':
          while zombieHealth > 0:
            damageValue = int(random.randint(1,4))
            question = input('Would you like to ATTACK or DEFEND?\n')
            if question == 'ATTACK':
              zombieStorage = zombieHealth
              zombieHealth = zombieStorage - damageValue
              if zombieHealth <= 0:
                zombieHealth = 0
                time.sleep(0.5)
                print('You attacked the zombie for '+str(damageValue)+' damage. It falls down to the floor, seemingly dead.')
                lvlstorage = 1
                time.sleep(0.5)
                continue
              time.sleep(0.5)
              print('You attacked the zombie for '+str(damageValue)+' damage. It has '+str(zombieHealth)+' health left.')
      
      def pickaxeAction(self):
        if item == 'pickaxe':

          while zombieHealth > 0:
            damageValue = int(random.randint(2,5))
            question = input('Would you like to ATTACK or DEFEND?\n')
            if question == 'ATTACK':
              zombieStorage = zombieHealth
              zombieHealth = zombieStorage - damageValue
              if zombieHealth <= 0:
                zombieHealth = 0
                time.sleep(0.5)
                print('You attacked the zombie for '+str(damageValue)+' damage. It has '+str(zombieHealth)+' health left.')
                lvlstorage = 1
                time.sleep(0.5)
                print('It falls down to the floor, seemingly dead.')
                continue
              time.sleep(0.5)
              print('You attacked the zombie for '+str(damageValue)+' damage. It has '+str(zombieHealth)+' health left.')
      
      def swordAction(self):  
        if item == 'sword':

          while zombieHealth > 0:
            damageValue = int(random.randint(4,7))
            question = input('Would you like to ATTACK or DEFEND?\n')
            if question == 'ATTACK':
              zombieStorage = zombieHealth
              zombieHealth = zombieStorage - damageValue
              if zombieHealth <= 0:
                zombieHealth = 0
                time.sleep(0.5)
                print('You attacked the zombie for '+str(damageValue)+' damage. It has '+str(zombieHealth)+' health left.')
                lvlstorage = 1
                time.sleep(0.5)
                print('It falls down to the floor, seemingly dead.')
                continue
              time.sleep(0.5)
              print('You attacked the zombie for '+str(damageValue)+' damage. It has '+str(zombieHealth)+' health left.')
      
      def axeAction(self):  
        if item == 'axe':

          while zombieHealth > 0:
            damageValue = int(random.randint(3,9))
            question = input('Would you like to ATTACK or DEFEND?\n')
            if question == 'ATTACK':
              zombieStorage = zombieHealth
              zombieHealth = zombieStorage - damageValue
              if zombieHealth <= 0:
                zombieHealth = 0
                time.sleep(0.5)
                print('You attacked the zombie for '+str(damageValue)+' damage. It has '+str(zombieHealth)+' health left.')
                lvlstorage = 1
                time.sleep(0.5)
                print('It falls down to the floor, seemingly dead.')
                continue
              time.sleep(0.5)
              print('You attacked the zombie for '+str(damageValue)+' damage. It has '+str(zombieHealth)+' health left.')
    
    battle = action()
          
    situation1 = input('\nYou wake up in a metal bunker. On your left, there is a SHOVEL. On your right, there is an old PICKAXE.\nSuddenly, you hear thumping at the door. You only have time to grab one item before the zombie breaks in. Which one will you pick?\n')  
    if situation1 == 'SHOVEL':
      item = 'shovel'
      print('You take the '+item+' and open the door carefully. The zombie charges in, hungry for human flesh.')
      battle.shovelAction()

    if situation1 == 'PICKAXE':
      item = 'pickaxe'
      print('You take the '+item+' and open the door carefully. The zombie charges in, hungry for human flesh.')
      battle.pickaxeAction()


  elif cont == 'N':
    again = input('OK. Would you like to CHOOSE AGAIN, or EXIT the game?')
    if again == 'CHOOSE AGAIN':
      time.sleep(1)
      print(' ')
      print('OK. Choosing again.')
      print(' ')
      time.sleep(1)
    elif again == 'EXIT':
      time.sleep(0.5)
      print(' ')
      print('OK. Exiting.')
      print(' ')
      time.sleep(0.5)
      quit()
