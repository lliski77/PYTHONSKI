room = 'starting'
coins = 0
game_running = True
 
while game_running:
  if room == 'starting':
    print("You find yourself in a strange place. To your left, a giant door with two coin slots. To your right, a large, cavernous room")
    print("If you want to try to unlock the door, enter '1'. To enter the big room, enter '2'")
 
    answer = input("1-2: ")
 
    if answer == "1":
      room = "door"
    elif answer == "2":
      room = "big"
    else:
      print("Invalid input entered")
 
  elif room == "door":
    if coins >= 2:
      print("You win!")
      game_running = False
    else:
      print("You need two coins to get through this door, but you only have " + str(coins) + "!")
      room = 'starting'
 
  elif room == "big":
    print("You have entered the massive room. To your left, you see a math puzzle. To your right, you see a word puzzle.")
    print("Enter '1' to do the math puzzle, enter '2' to do the word puzzle, enter '3' to go back to the starting room")
 
    answer = input("1-3: ")
 
    if answer == "1":
      room = "math"
    elif answer == "2":
      room = "word"
    elif answer == "3":
      room = "starting"
    else:
      print("Invalid input entered")
 
  elif room == "math":
    print("You see in front of you the following puzzle:")
    print("3 + 4 * 2")
    print("Choose your answer below:")
    print("a: 8")
    print("b: 11")
    print("c: 14")
    print("d: 18")
 
    answer = input("a-d: ").lower()
 
    if answer == "a" or answer == "c" or answer == "d":
      print("Sorry, that is incorrect")
    elif answer == "b":
      print("That is correct! You have been awarded 1 coin")
      coins += 1
      room = "big"
    else:
      print("Invalid input entered")
 
  elif room == "word":
    print("You see in front of you the following puzzle:")
    print("Descramble the name of an animal: nnipuge")
 
    answer = input("Type out your answer: ").lower()
 
    if answer == "penguin":
      print("That's correct! One coin has been awarded")
      coins += 1
      room = "big"
    else:
      print("Sorry, that is incorrect")
 
  print("")