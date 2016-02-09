#need to make this library
import gamestats

import random

level = gamestats.thisuser
inventory = gameestats.thisuser
heath = (level * 10) + 100

enemies = {"Ogre" : 40, "elf" : 30, "bear" : 60}

iterator = random.choice(list(enemies.keys()))
enemy = enemies[iterator]
enemyHealth = enemies.get(enemy)

while health > 0:
  print (enemy, "has decided to fight you!")
  print "Enemy health : %s" %  dict.get(enemy)
  break
