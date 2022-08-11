#coding: utf-8
from curses import flushinp
import time, random, sys, os
def main():
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
      
      class retr:
        def retry(self):
          retry = input('Would you like to try again? Y/N\n')
          if retry =='Y':
           main()
          elif retry == 'N':
           print('OK. Exiting.')
           quit()
      r = retr()

      parryChance = 0
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
      class fortifiedzombAttr:
        zombieHealth = 50
        zombieStorage = 0
        zombieName = 'Fortified Zombie'
      class bosszombAttr:
        zombieHealth = 100
        zombieStorage = 0
        zombieName = 'Cameron'
      
      def zombAttack(self):
        zombieStrength = random.randint(0,1) #2,4
        plrAttr.playerStorage = plrAttr.playerHealth
        plrAttr.playerHealth = plrAttr.playerStorage - zombieStrength
        if plrAttr.playerHealth <= 0:
          plrAttr.playerHealth = 0
          time.sleep(0.5)
          print('\nIt strikes you for ' + str(zombieStrength) + ' damage. You fall over, dead.')
          time.sleep(0.5)
          r.retry()
        time.sleep(1)
        print('It attacks you for '+ str(zombieStrength) + ' damage. You have ' + str(plrAttr.playerHealth) +' health left.')
        time.sleep(1)
      
      def fortifiedZombAttack(self):
        zombieStrength = random.randint(0,1) #3,5
        plrAttr.playerStorage = plrAttr.playerHealth
        plrAttr.playerHealth = plrAttr.playerStorage - zombieStrength
        if plrAttr.playerHealth <= 0:
          plrAttr.playerHealth = 0
          time.sleep(0.5)
          print('\nThe zombie strikes you for ' + str(zombieStrength) + ' damage. You fall over, dead.')
          time.sleep(0.5)
          r.retry()
        time.sleep(1)
        print('The '+ str(fortifiedzombAttr.zombieName) +' attacks you for '+ str(zombieStrength) + ' damage. You have ' + str(plrAttr.playerHealth) +' health left.')
        time.sleep(1)
      
      def bossZombAttack(self):
        zombieStrength = random.randint(5,7)
        plrAttr.playerStorage = plrAttr.playerHealth
        plrAttr.playerHealth = plrAttr.playerStorage - zombieStrength
        if plrAttr.playerHealth <= 0:
          plrAttr.playerHealth = 0
          time.sleep(0.5)
          print('\nCameron strikes you for ' + str(zombieStrength) + ' damage. You fall over, dead.')
          time.sleep(0.5)
          r.retry()
        time.sleep(1)
        print('The '+ str(bosszombAttr.zombieName) +' attacks you for '+ str(zombieStrength) + ' damage. You have ' + str(plrAttr.playerHealth) +' health left.')
        time.sleep(1)

      class action:
        def shovelAction(self):
          if item == 'shovel':
            zombAttr.zombieHealth = 20
            zombAttr.zombieStorage = 0
            while zombAttr.zombieHealth > 0:
              playerStrength = random.randint(19,20)#1,3
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                zombAttr.zombieStorage = zombAttr.zombieHealth
                zombAttr.zombieHealth = zombAttr.zombieStorage - playerStrength
                if zombAttr.zombieHealth <= 0:
                  zombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('\nYou attack the ' + zombAttr.zombieName + ' for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue 
                time.sleep(0.5)
                print('\nYou attack the ' + zombAttr.zombieName +' for '+str(playerStrength)+' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
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
                  zombAttack(self)
                  time.sleep(0.5)

        def pickaxeAction(self):
          if item == 'pickaxe':
            zombAttr.zombieHealth = 20
            zombAttr.zombieStorage = 0
            while zombAttr.zombieHealth > 0:
              playerStrength = random.randint(2,4)
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                zombAttr.zombieStorage = zombAttr.zombieHealth
                zombAttr.zombieHealth = zombAttr.zombieStorage - playerStrength
                if zombAttr.zombieHealth <= 0:
                  zombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('\nYou attack the ' + zombAttr.zombieName + ' for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  continue
                time.sleep(0.5)
                print('\nYou attack the ' + zombAttr.zombieName +' for '+str(playerStrength)+' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
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
                  zombAttack(self)
                  time.sleep(0.5)
        
        def knifeAction(self):  
          if item == 'knife':
            fortifiedzombAttr.zombieHealth = 50
            fortifiedzombAttr.zombieStorage = 0
            while fortifiedzombAttr.zombieHealth > 0:
              playerStrength = random.randint(49,50)#4.6
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                fortifiedzombAttr.zombieStorage = fortifiedzombAttr.zombieHealth
                fortifiedzombAttr.zombieHealth = fortifiedzombAttr.zombieStorage - playerStrength
                if fortifiedzombAttr.zombieHealth <= 0:
                  fortifiedzombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('\nYou attack the ' + fortifiedzombAttr.zombieName + ' for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue 
                time.sleep(0.5)
                print('\nYou attack the ' + fortifiedzombAttr.zombieName +' for '+str(playerStrength)+' damage. It has '+str(fortifiedzombAttr.zombieHealth)+' health left.')
                fortifiedZombAttack(self)
              if question == 'DEFEND':
                fortifiedzombAttr.zombieStorage = fortifiedzombAttr.zombieHealth
                fortifiedzombAttr.zombieHealth = fortifiedzombAttr.zombieStorage - playerStrength
                parryChance = random.randint(1,100)
                if parryChance <= 45:
                  print('You successfully defend the attack, giving you an opening. You strike, dealing ' + str(playerStrength)+ ' damage. It has '+str(fortifiedzombAttr.zombieHealth)+' health left.')
                  time.sleep(0.5)
    
                if parryChance > 45:
                  print('You attempt to defend the attack, but fail.')
                  fortifiedZombAttack(self)
                  time.sleep(0.5)
        
        def gunAction(self):  
          if item == 'gun':
            fortifiedzombAttr.zombieHealth = 50
            fortifiedzombAttr.zombieStorage = 0
            while fortifiedzombAttr.zombieHealth > 0:
              playerStrength = random.randint(49,50)#3,8
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                fortifiedzombAttr.zombieStorage = fortifiedzombAttr.zombieHealth
                fortifiedzombAttr.zombieHealth = fortifiedzombAttr.zombieStorage - playerStrength
                if fortifiedzombAttr.zombieHealth <= 0:
                  fortifiedzombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('\nYou attack the ' + fortifiedzombAttr.zombieName + ' for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue 
                time.sleep(0.5)
                print('\nYou attack the ' + fortifiedzombAttr.zombieName +' for '+str(playerStrength)+' damage. It has '+str(fortifiedzombAttr.zombieHealth)+' health left.')
                fortifiedZombAttack(self)
              if question == 'DEFEND':
                fortifiedzombAttr.zombieStorage = fortifiedzombAttr.zombieHealth
                fortifiedzombAttr.zombieHealth = fortifiedzombAttr.zombieStorage - playerStrength
                parryChance = random.randint(1,100)
                if parryChance <= 49:
                  print('You successfully defend the attack, giving you an opening. You strike, dealing ' + str(playerStrength)+ ' damage. It has '+str(fortifiedzombAttr.zombieHealth)+' health left.')
                  time.sleep(0.5)
    
                if parryChance > 49:
                  print('You attempt to defend the attack, but fail.')
                  fortifiedZombAttack(self)
                  time.sleep(0.5)

        def karambit(self):
          if item == 'karambit':
            bosszombAttr.zombieHealth = 100
            bosszombAttr.zombieStorage = 0
            while bosszombAttr.zombieHealth > 0:
              playerStrength = random.randint(5,10)
              question = input('Would you like to ATTACK or DEFEND?\n')
              if question == 'ATTACK':
                bosszombAttr.zombieStorage = bosszombAttr.zombieHealth
                bosszombAttr.zombieHealth = bosszombAttr.zombieStorage - playerStrength
                if bosszombAttr.zombieHealth <= 0:
                  bosszombAttr.zombieHealth = 0
                  time.sleep(0.5)
                  print('\nYou attack ' + bosszombAttr.zombieName + ' for '+str(playerStrength)+' damage. It falls down to the floor, seemingly dead.')
                  plrAttr.zombie_storage = plrAttr.zombies_killed
                  plrAttr.zombies_killed = plrAttr.zombie_storage + 1
                  time.sleep(0.5)
                  continue 
                time.sleep(0.5)
                print('\nYou attack ' + bosszombAttr.zombieName +' for '+str(playerStrength)+' damage. It has '+str(bosszombAttr.zombieHealth)+' health left.')
                zombAttack(self)
                if question == 'DEFEND':
                  bosszombAttr.zombieStorage = bosszombAttr.zombieHealth
                  bosszombAttr.zombieHealth = bosszombAttr.zombieStorage - playerStrength
                  parryChance = random.randint(1,100)
                  if parryChance <= 49:
                    print('You successfully defend the attack, giving you an opening. You strike, dealing ' + str(playerStrength)+ ' damage. It has '+str(zombAttr.zombieHealth)+' health left.')
                    time.sleep(0.5)
  
                if parryChance > 49:
                  print('You attempt to defend the attack, but fail.')
                  bossZombAttack(self)
                  time.sleep(0.5)
          
      battle = action()
            
      situation1 = input('\nYou wake up in a metal bunker. On your left, there is a rusty SHOVEL. On your right, there is an old PICKAXE.\nSuddenly, you hear thumping at the door. You only have time to grab one item before the zombie breaks in. Which one will you pick?\n')  
      if situation1 == 'SHOVEL':
        item = 'shovel'
        time.sleep(0.5)
        print('\nYou take the '+item+' and open the door carefully. The zombie charges in, hungry for human flesh.')
        battle.shovelAction()

      if situation1 == 'PICKAXE':
        item = 'pickaxe'
        time.sleep(0.5)
        print('\nYou take the '+item+' and open the door carefully. The zombie charges in, hungry for human flesh.')
        battle.pickaxeAction()
      
      time.sleep(1)
      print('\nYou wipe your weapon on your tattered shirt, before looking at your available options. Going outside is risky, so you decide to head down into the sewers.\n')
      time.sleep(2)
      print('\033[1mChapter One: The Beginning \033[0m')
      time.sleep(2)
      print('\nYou run downstairs and realize you are in the dark. You cannot see anything. You can hear noises above, and they sound like zombies. Luckily, you are below ground. You stumble on something and fall over. You realize it was a brick and keep walking. After a few steps, you hit a wall. You look to your left and see another passage. You tap the wall and find it is hollow.')
      time.sleep(1)
      situation2 = input('You can either try and BREAK down the wall with the brick and find out what is behind it or you can WALK past the wall.\n')
      
      if situation2 == 'BREAK':
        print('You successfully break down the wall, only to find it is a zombie colony! You try to run but they catch your legs. You are dragged back into the colony and eaten alive. ')
        r.retry()
      elif situation2 == 'WALK':
        time.sleep(1)
      print('\nYou decide to keep walking. You hear footsteps above and hope that they don\'t start digging. The deeper you go the more undergrowth you find. You eventually arrive at a door with a red light above it. You realize the door has exposed wiring that could electrocute you if you touch the door with bare skin. You could try and divert the current to a different wire and potentially allowing you to safely exit the door.\n')
      time.sleep(1)
      situation3 = input('You can either DIVERT the current or try to OPEN the door.\n')

      if situation3 == 'OPEN':
        print('\nYou choose to risk opening the door. You take a few steps back and put your shoulder forward. You run into the door and fall through with a numb shoulder. In front of you sits the basement of an office building.')
        time.sleep(0.5)
      elif situation3 == 'DIVERT':
        choicerng = random.randint(1,100)
        if choicerng >= 30:
          print('\nIn front of you sits the basement of an office building. You choose to divert the current. You walk over to the wiring and try diverting the current. You twist the wires and join them together. You have made the door safe to open! You open the door and, after many hours in the dark, you emerge into the basement of an office building.')
          time.sleep(0.5)
        elif choicerng < 70:
          print('\nYou choose to divert the current. You walk over to the wiring and try diverting the current. You twist the wires and join them together. Suddenly, with sharp buzz, they electrocute you, frying your brain instantly.')
          r.retry()
      print('You continue walking, hands outstretched in a dark and ominous surrounding. You see a door with light pooling in from the cracks. Your foot kicks something which skids just ahead of you. You walk blindly towards and pick it up. You recognise it as a handgun.  You also see something reflecting the light. You tread towards it, carefully. You realize it is a knife.')
      time.sleep(1)
      situation4 = input('Both weapons are better than your ' + item + '. Should you choose the KNIFE or the HANDGUN?\n')
      if situation4 == 'KNIFE':
        item = 'knife'
        time.sleep(1)
        print('You pick up the sharp, metal knife and go up the stairs. As you open the door, you see a hoard of zombies. You ready your knife, as this will be a tough fight.')
        time.sleep(0.5)
        battle.knifeAction()
        time.sleep(0.5)
        print('The first zombie goes down. You hide behind a doorway to nurse your wounds, healing yourself fully. Another zombie leaps at you from around the corner.')
        time.sleep(0.5)
        plrAttr.playerHealth = 20
        plrAttr.playerStorage = 0
        battle.knifeAction()
        time.sleep(0.5)
        print('You kick the zombie to the side as you inject yourself with a healthy dose of epinephrine, giving you the energy needed to keep fighting.')
        time.sleep(0.5)
        print('A zombie lunges for your legs, but you jump over it and stab it ruthlessly. A third zombie surprises you as you jump back.')
        time.sleep(0.5)
        plrAttr.playerHealth = 20
        plrAttr.playerStorage = 0
        battle.knifeAction()
        time.sleep(0.5)
        print('You look around. There are no more zombies left. You head up the ladder into the light.')
      
      elif situation4 == 'HANDGUN':
        item = 'gun'
        time.sleep(1)
        print('You pick up the handgun and go up the stairs. As you open the door, you see a hoard of zombies. You load your gun. This will be a tough fight.')
        time.sleep(0.5)
        battle.gunAction()
        time.sleep(0.5)
        print('The first zombie goes down. You hide behind a doorway to nurse your wounds, healing yourself fully. Another zombie leaps at you from around the corner.')
        time.sleep(0.5)
        battle.gunAction()
        time.sleep(0.5)
        print('You kick the zombie to the side as you inject yourself with a healthy dose of epinephrine, giving you the energy needed to keep fighting.')
        time.sleep(0.5)
        print('A zombie lunges for your legs, but you jump over it and shoot at it ruthlessly. A third zombie surprises you as you jump back.')
        time.sleep(0.5)
        battle.gunAction()
        time.sleep(0.5)
        print('You look around. There are no more zombies left. You head up the ladder into the light.')
      
      time.sleep(5)
      print('\033[1m\nChapter Two:\n\033[0m')
      cutscene1 = 'You warily take a step outside. With every step taken, your energy level decreases as if it were being poured out of you. All you want is some food... Some IKEA meatballs sound good right now, but that is too far away if you want to remain alive. Your mouth feels dry. You know you can\'t take any chances with the water; it is only too likely that it is infected. Now, you hear the nightmarish complaints of the \'things\' only a few yards away. \'Bloody forei-foreigners!\' they groan. Another mumbles, “The signal t-to-tower! Please! Camer-…” What? What did the zombie say? Was that...? No, it can\'t be... The zombie bursts leaving a single leg, balancing on its own. Never mind.  Once again, you get up for the final stand to reach the signal tower. But wait... Something catches your eye. A scroll sprouts out of the leg left behind by the zombie. There might be something important. You stumble towards it and read.'
      for char in cutscene1: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
      time.sleep(1)
      cutscene2 = '\n\n"The signal tower sprouted from the earthen ground. I was there when it happened; I was there at it all. I was at the IKEA Café at the time. That was my mistake... These spores must have been embedded within the gelatinous spheres of beef. The moment I took a bite of the tainted meat, I began to feel changes. The urge to eat the scroll was too strong was too strong; I couldn\'t resist. Suddenly, I heard the cry of a being within the signal tower. I knew I no longer had the strength to end this, so I leave the fate of this world in your hands, fellow reader. You must do this on your own. "'
      for char in cutscene2: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
      time.sleep(1)
      cutscene3 = '\n\nThe one thing you came here to do is to destroy the source of the spores. The Signal Tower. Now, all you need to do is to find it.  You limp to the end of the room to find a button in front of a door. Whatever there is behind it, you know there is no going back... '
      for char in cutscene3: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
      time.sleep(1)
      cutscene4 = 'The door swiftly slides open with your trembling hand making contact with the button. \n\nWhat lies on the other side makes you gasp... \n\nA being lies lazily on the cold stone floor against the wall - it is huge. They have grown unnaturally obese; their stomach bursting out of an incredibly strained shirt. That is when you realize... \n\nIt\'s Cameron Clark! \n\nHe seemingly emits spores out of his enlarged hands, whilst he painfully murmurs \'Black Boys Play the Classics\'.'
      for char in cutscene4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
      cutscene5 = ' \n\nOne last fight... '
      for char in cutscene5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
      time.sleep(3)
      print('\nYou see a karambit lying on the ground. You pick it up, determined. It all ends here.')
      time.sleep(1)
      print('\n' * 20)
      item = 'karambit'
      time.sleep(5)
      battle.karambit()
      time.sleep(2)
      print('\n' * 20)
      imlosingmysanity = input('You can either...\WALK away now and leave \n OR\nYou can STAY and rest.')
      if imlosingmysanity == 'WALK':
        time.sleep(1)
        print('Your trembling legs turn, and you walk away. You slip through the sliding doors, and you meet with the outer world once more. The dying light fades under the emerging darkness in the sky. You feel guilty for leaving Cameron to rot away in the signal tower. \n\nThat\'s when you hear it... The ominous rumble of the tower. \n\nThe weight of poor Cameron must have been too much for the foundations. A large crack emerges from the bottom of the tower, running up the concrete. \n\nIt falls. \n\nNow you regret your decisions. You were wrong, you failed, you couldn\'t do it, you were always doomed to die like this - with pain and suffering and guilt for not being there for your dear friend Cameron. \n\nThe looming shadow grows bigger to swallow you whole... ')
      elif imlosingmysanity == 'STAY':
        time.sleep(1)
        print('Cameron Clarke sits on the floor, stomach open like the mouth of a cavern, fingers twitching. You feel remorse. Cameron was a good guy in his years of poetry. \n\nYou see, after Cameron won second place in the competition, he felt anger and frustration. In the end, he decided life did not deserve \'Black Boys Play the Classics\' and resorted to a new life without pain or suffering. No second place, no poetry. Just an eternity of IKEA meatballs. That was all he wanted... But with selfish choices, come consequences. In return for his endless supply of meatballs, he turned into what he is now; a sack of flesh where the meatballs manifested into the infectious spores that turned the English. \n\nNow, you sit beneath the dying sun that sinks under the horizon. You left the world as a better place. The zombies are gone, the world is safe, and the IKEA Meatball Manufacturers will be fired.  \n\nEverything turns to darkness... ')
      time.sleep(5)
      print('\n' * 20)
      time.sleep(3)
      tysm = 'THANK YOU FOR PLAYING'
      for char in tysm:
        sys.stdout.write(char)
        sys.stdout.flush
        time.sleep(1)
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