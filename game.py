import random
 
name = input("What is your name, castaway? ")
room = "dock"
hp = 8
oil = 8
items = []
end = False
 
while not end and hp > 0 and oil > 0:
  print("\nHP:", hp, "| Oil:", oil, "| Items:", items)
 
  if room == "dock":
    a = input("Your boat is wrecked. A lighthouse looms. 1) search boat 2) go inside: ")
    if a == "1" and "oar" not in items:
      items.append("oar")
      print("You found an oar!")
    elif a == "2":
      room = "hall"
 
  elif room == "hall":
    a = input("1) cellar 2) library 3) lamp room: ")
    room = {"1": "cellar", "2": "library", "3": "lamp"}.get(a, room)
 
  elif room == "cellar":
    if "key" in items:
      print("The cellar is empty now.")
    else:
      roll = random.randint(1, 6)
      if "oar" in items:
        roll += 1
      print("Rats attack! You rolled", roll)
      if roll >= 4:
        items.append("key")
        print("You win and find a brass key!")
      else:
        hp -= 3
        print("They bite you! -3 HP")
    room = "hall"
 
  elif room == "library":
    a = input("A ghost offers a gamble: risk 2 HP for oil. 1) roll 2) leave: ")
    if a == "1":
      if random.randint(1, 6) > 3:
        oil += 5
        print("The ghost refills your lantern! +5 oil")
      else:
        hp -= 2
        print("The ghost shocks you! -2 HP")
    elif a == "2":
      room = "hall"
 
  elif room == "lamp":
    if "key" not in items:
      print("The door is locked. You need a key.")
      room = "hall"
    else:
      a = input("1) light the lamp 2) smash the lamp: ")
      if a == "1":
        print("ENDING: Hero of the Coast! Ships are saved.")
        end = True
      elif a == "2":
        print("ENDING: The Dark Keeper. The lighthouse is yours forever.")
        end = True
 
  oil -= 1
 
if not end and hp <= 0:
  print("ENDING: The rats win. Lost to the storm.")
elif not end:
  print("ENDING: Your lantern dies. Lost in the dark.")
 
print("Thanks for playing,", name)
