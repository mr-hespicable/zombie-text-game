def main():
  import time, random, sys, os
  os.system('clear')
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
        time.sleep(0.08) #0.08
      
      time.sleep(2)

      message2 = '\nA zombie apocalypse has broken out in England. You must reach the signal tower emitting the dangerous spores that are infecting the public.\nUnfortunately, the signal tower is located in the IKEA warehouse full of English zombies yelling ' '"Bloody foreigners!"' ' Sadly, you are not from England, so you are at great risk to these zombies. You will have to make different choices that affect the story, with many resulting in death.\n'
      for char in message2: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0001) #0.03

      time.sleep(1)
      message3 = "Welcome to the Apocolypse.\n"
      for char in message3: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0001) #0.2
      
      class plrAttr:
        playerHealth = 20
        playerStorage = 0
        lvlstorage = 1
        playerlvl = 0
        zombies_killed = 0
        zombie_storage = 0

      class zombAttr:
        zombieHealth = 20
        zombieStorage = 0 
        zombieName = 'Zombie'
      def zombAttack(self):
        zombieStrength = random.randint(3,5)
        plrAttr.playerStorage = plrAttr.playerHealth
        plrAttr.playerHealth = plrAttr.playerStorage - zombieStrength
        if plrAttr.playerHealth <= 0:
          plrAttr.playerHealth = 0
          time.sleep(0.5)
          print('\nThe zombie strikes you for ' + str(zombieStrength) + ' damage. You fall over, dead.')
          time.sleep(0.5)
          retry = input('Would you like to try again? Y/N\n')
          if retry =='Y':
            main()
          elif retry == 'N':
            print('OK. Exiting.')
            quit()
        time.sleep(1)
        print('\nThe '+ str(zombAttr.zombieName) +' attacks you for '+ str(zombieStrength) + ' damage. You have ' + str(plrAttr.playerHealth) +' health left.')
        time.sleep(1)
          

      class action:
        def shovelAction(self):
          if item == 'shovel':
            while zombAttr.zombieHealth > 0:
              playerStrength = random.randint(1,3)
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                zombAttr.zombieStorage = zombAttr.zombieHealth
                zombAttr.zombieHealth = zombAttr.zombieStorage - playerStrength
                if zombAttr.zombieHealth <= 0:
                  zombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('You attack the ' + zombAttr.zombieName + ' for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue 
                time.sleep(0.5)
                print('You attack the ' + zombAttr.zombieName +' for '+str(playerStrength)+' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
                zombAttack(self)
              
              if question == 'DEFEND':
                zombAttr.zombieStorage = zombAttr.zombieHealth
                zombAttr.zombieHealth = zombAttr.zombieStorage - playerStrength
                parryChance = random.randint(1,100)
                if parryChance <= 45:
                  print('You successfully defend the attack, giving you an opening. You strike, dealing ' + str(playerStrength)+ ' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
                  time.sleep(0.5)
    
                if parryChance > 45:
                  print('You attempt to defend the attack, but fail.')
                  time.sleep(0.5)

        
        def pickaxeAction(self):
          if item == 'pickaxe':
            while zombAttr.zombieHealth > 0:
              playerStrength = random.randint(2,4)
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                zombAttr.zombieStorage = zombAttr.zombieHealth
                zombAttr.zombieHealth = zombAttr.zombieStorage - playerStrength
                if zombAttr.zombieHealth <= 0:
                  zombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('You attacked the zombie for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue
                time.sleep(0.5)
                print('You attacked the zombie for '+str(playerStrength)+' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
                zombAttack(self)
        
        def knifeAction(self):  
          if item == 'knife':
            while zombAttr.zombieHealth > 0:
              playerStrength = random.randint(4,6)
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                zombAttr.zombieStorage = zombAttr.zombieHealth
                zombAttr.zombieHealth = zombAttr.zombieStorage - playerStrength
                if zombAttr.zombieHealth <= 0:
                  zombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('You attacked the zombie for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue
                time.sleep(0.5)
                print('You attacked the zombie for '+str(playerStrength)+' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
                zombAttack(self)
        
        def axeAction(self):  
          if item == 'axe':
            while zombAttr.zombieHealth > 0:
              playerStrength = random.randint(3,8)
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                zombAttr.zombieStorage = zombAttr.zombieHealth
                zombAttr.zombieHealth = zombAttr.zombieStorage - plrAttr.playerStrength
                if zombAttr.zombieHealth <= 0:
                  zombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('You attacked the zombie for '+str(plrAttr.playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue
                time.sleep(0.5)
                print('You attacked the zombie for '+str(plrAttr.playerStrength)+' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
                zombAttack(self)
      
      battle = action()
            
      situation1 = input('\nYou wake up in a metal bunker. On your left, there is a rusty SHOVEL. On your right, there is an old PICKAXE.\nSuddenly, you hear thumping at the door. You only have time to grab one item before the zombie breaks in. Which one will you pick?\n')  
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
main()
