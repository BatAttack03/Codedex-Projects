
import random

# Plot -> You wake up in the shadow realm. You cannot escape, but you still have hope. You could battle the evil leader of this realm and cleanse it with light, or steal their power and crown yourself as their ruler.

#~~Ch1~~
def start():
  print('Chapter 1: Rebirth')
  print('You wake up in a cold, dark place. Oh no, you must be dead!')
  Q1()

# ~Q1~
def Q1():
  name = input("What is your name? ")
  print('Welcome to the Shadow Realm '+name+'!')
  role()

# ~Q2~
def role():
  print('What was your role before you died?')
  print(' 1) Knight')
  print(' 2) Mage')
  print(' 3) Rogue')
  print(' 4) Noble')
  answer_1 = int(input('Enter number: '))
  if answer_1 == 1:
    print('Ahh, a noble knight has reached the shadows! 🗡')
    path()
  elif answer_1 == 2:
    print('Shadow wizard money gang 🧙‍♂️😎')
    path()
  elif answer_1 == 3:
    print("An assassin! You'll fit in well. 👥")
    path()
  elif answer_1 == 4:
    print("Oh! What a delight it is to bask in the honor of royalty! 👑")
    path()
  else:
    print("That's not an option 😡 Try again.")
    role()
    
# ~Q3~
def path():
  print("You're stuck here for eternity 😨 Will you choose to bring light to this realm, or destroy its ruler and steal the crown?")
  print(' 1) Cleanse')
  print(' 2) Rule')
  answer_2 = int(input('Enter number: '))
  if answer_2 == 1:
    print('A noble route!')
    lost_soul()
  elif answer_2 == 2:
    print("I hope you're ready to rule!")
    lost_soul()
  else:
    print("That's not an option 😡 Try again.") 
    path()

# ~Q4~
def lost_soul():
  print("As you walk along the path ahead, you spot a shadow being like you, but this one looks pretty erratic. Maybe they just need a hug?")
  print(" 1) Hug")
  print(" 2) Don't hug")
  answer_3 = int(input("Enter number: "))
  if answer_3 == 1:
    print ("The shadow says in a low growl,")
    print('"The happy sunshine. In the walls. Take it and be a god!!"')
    print("With that, the erratic shadow runs away into the darkness. Maybe you should investigate this 'sunshine.'")
    castle_gate()
  elif answer_3 == 2:
    print("The erratic shadow points at you and screams in a gritty, panicked voice, ")
    print('"AH! MEATLESS!! DARKNESS!!!')
    print("The shadow runs away. That was weird...")
    castle_gate()
  else:
    print("That's not an option 😡 Try again.")
    lost_soul()

# ~Q5~
def castle_gate():
  print("That was scary, but you're reaching the entrance to the city. Hopefully these people will be more civilized.")
  print("You approach the guards at the gate and ask if you can enter. They look you up and down, then look at each other, then back at you. They sway their heads no.")
  print("How will you convince them to let you in?")
  print(" 1) Tell them you're royalty, and deserve to be let into the city.")
  print(" 2) Tel them you will rip their heads off.")
  print(" 3) Tell them you're a lost soul seeking shelter from the outerlands.")
  answer_4 = int(input("Enter number: "))
  if answer_4 == 1:
    persuasion_check = random.randint(1, 3)
    if persuasion_check == 1:
      print("Your attempt to trick the guards was successful! You pass through the gate with ease.")
      in_the_city()
    elif persuasion_check == 2:
      print("The guards maintain their stone cold demeanor. You won't get in with trickery. Maybe you can try again?")
      castle_gate()
    else:
      print("The guards maintain their stone cold demeanor. You won't get in with trickery. Maybe you can try again?")
      castle_gate()
  elif answer_4 == 2: 
    intimidation_check = random.randint(1, 3)
    if intimidation_check == 1:
      print("Your attempt to intimidate the gaurds was successful! They're shaking in their boots 😓")
      in_the_city()
    elif intimidation_check == 2:
      print("Your attempt to intimidate the guards was unsuccessful. They laugh in your face! Try again?")
      castle_gate()
    else:
      print("Your attempt to intimidate the guards was unsuccessful. They laugh in your face! Try again?")
      castle_gate()
  elif answer_4 == 3:
      print("The guards both grunt in unison and open the gate. You pass through the gate wih ease.")
      in_the_city()
  else:
    print("That's not an option 😡 Try again.")
    castle_gate()

# ~Q6~
def in_the_city():
  print("Chapter 2: The Power of the People")
  print("You walk into the city and you notice a flyer by your foot. It reads, " + '"Are you unhappy with the way the authorities treat you? If so, come visit [address] alone. "' + "Will you visit the address?")
  print(" 1) Yes")
  print(" 2) No")
  answer_5 = int(input("Enter number: "))
  if answer_5 == 1:
    rebellion()
  elif answer_5 == 2:
    print("You decide it would be a waste of time and head straight to the castle.")
    castle_gate()
  else:
    print("That's not an option 😡 Try again.")
    in_the_city()

# ~Q7~
def rebellion():
  print("You find the address. It's at a place called " + "'The Sleeping Goliath Inn.'" + " You approach the bartnender and ask about the flyer. He shushes you and leads you to a back room where two others are gathered around a table.")
  print("They look up at you, and the bartender says you must be the chosen one. He asks if you would aid in their efforts to bring light to the land and presents a crystal with a shining star in the center.")
  print("This must be the object you can use to save this realm from evil. Will you take it and save them, or destroy it and preserve your future as a ruler?")
  print(" 1) Help them")
  print(" 2) Destroy the crystal")
  answer_6 = int(input("Enter number: "))
  if answer_6 == 1:
    print("They rejoice and give you the crystal. You walk out of the inn with determination.")
    castle_guards()
  elif answer_6 == 2:
    print("You throw the crystal on the ground and crush it underneath your foot. The star with in it still lies shining on the floor before fizzling out.")
    print("The members of the rebellion scream at you and throw you out. At least you've protected your future...")
    castle_guards()
  else:
    print("That's not an option 😡 Try again.")
    rebellion()

# ~Q8~
def castle_guards():
  print("You walk through the city and find a castle. This must be where their ruler lives, it's swarmed with armed guards.")
  print("How will you get through them?")
  print(" 1) Fight")
  print(" 2) Fireball")
  print(" 3) Sneak attack")
  print(" 4) Persuade")
  answer_7 = int(input("Enter number: "))
  if answer_7 == 1:
    print("You fight your way through the gaurds like a true knight and reach the throne room where the ruler resides.")
    final_battle_turn1()
  elif answer_7 == 2:
    print("You cast fireball and all the guards are burnt to a crisp. You walk up the stairs to the throne room.")
    final_battle_turn1()
  elif answer_7 == 3:
    print("You take each guard down. One. By. One. You sneak into the throne room and confront the ruler.")
    final_battle_turn1()
  elif answer_7 == 4:
    print("You find a guard and explain that you have a meeting with their ruler, the nobility in your voice is enough to get you to the throne room without violence.")
    final_battle_turn1()
  else:
    print("That's not an option 😡 Try again.")
    castle_guards()

# ~Q9~
def final_battle_turn1():
  print("The evil ruler of the Shadow Realm looks up at you from their throne.")
  print('"How dare you enter my castle uninvited. I will make you pay."')
  print("The ruler says in an aged voice. You won't accept a threat from a fossil!")
  print("They stand up and use their sceptor to cast a holding spell on you. You can't move, what do you do?")
  print(" 1) Struggle until you break the spell")
  print(" 2) Stay calm and wait for the spell to break on its own.")
  answer_8 = int(input("Enter number: "))
  if answer_8 == 1:
    print("The spell breaks and you can move again!")
    final_battle_turn2()
  elif answer_8 == 2:
    print("The ruler uses his sceptor to bonk you on the head while you're immobilized 😕 ")
    final_battle_turn2()
  else:
    print("That's not an option 😡 Try again.")
    final_battle_turn1()
  
# ~Q10~
def final_battle_turn2():
  print("You can move again! You use this opportunity to attack the ruler. They fall to the ground and their crown falls.")
  print("You stand above them and deliver the final attack. The ruler lets out a loud wail before they perish.")
  print("Do you have the crystal?")
  print(" 1) Yes")
  print(" 2) No") 
  answer_9 = int(input("Enter number: "))
  if answer_9 == 1:
    print("You raise the crystal. Sunshine floods the room and pours out the windows. After a few moments, the crystal flies out of your hands and into the sky. The sun is back!")
    crown()
  elif answer_9 == 2:
    print("The skies remain dark and the curse is still present.")
    crown()
  else:
    print("That's not an option 😡 Try again.")
    final_battle_turn2()

# ~Q11~
def crown():
  print("You look down at the expired tyrant. Will you take their crown?")
  print(" 1) Yes")
  print(" 2) No")
  answer_10 = int(input("Enter number: "))
  if answer_10 == 1:
    print("You crown yourself and sit in the throne. Hail to the king baby! 👑")
    end()
  elif answer_10 == 2:
    print("You leave the crown on the floor, it's not your decision to make.")
    peoples_decision()
  else:
    print("That's not an option 😡 Try again.")
    crown()

# ~Q12~
def peoples_decision():
  print("You're the only one to walk out of the castle alive. It seems that the citizens of this city heard the final cry of their ruler, and now know you are the one who did it.")
  print("The rebels run to you and ask if you would like to take the ruler's place. Will you accept?")
  print(" 1) Yes")
  print(" 2) No")
  answer_11 = int(input("Enter number: "))
  if answer_11 == 1:
    print("You accept their offer and reign over the realm!")
    end()
  elif answer_11 == 2:
    print("You do not accept their offer. You have different plans here.")
    end()
  else:
    print("That's not an option 😡 Try again.")
    peoples_decision()

def end():
  print("~The End~")
  print("Thank you for playing!")

start()