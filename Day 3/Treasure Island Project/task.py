print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("""You are in a enchanted forest and you are chased by an angry rabbit.
In front of you, you have 2 paths: one goes to the left,
the other one to the right. Which one do you choose?\n""")
if left_or_right == "left" or left_or_right == "Left":
    swim_or_wait = input("""You have survived the angry rabbit,
and you reach a black lake.You have to choose again, swim
or wait?
Please enter your choice:\n""")
    if swim_or_wait == "wait" or swim_or_wait == "Wait":
        red_blue_yellow = input("""Because you have made the right choice an eagle comes and fly you over
across the lake.You are now in front of the castle.
In front of you there are three doors, a red one, a blue and a yellow.
Which door do you choose? Please enter your choice:\n""")
        if red_blue_yellow == "yellow" or red_blue_yellow == "Yellow":
            print("You win! The castle door opens and the treasure is all yours.")
        elif red_blue_yellow == "red" or red_blue_yellow == "Red":
            print("Burned by fire.Game Over.")
        elif red_blue_yellow == "blue" or red_blue_yellow == "Blue":
            print("Eaten by beasts.Game over.")
        else:
            print("Please choose one of the three colors (blue,red, yellow)")

    else:
        print("Attacked by trout.Game over.")
else:
    print("Fall into a hole. Game over.")

