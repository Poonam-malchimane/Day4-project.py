import random
rock = '''              _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
                     
'''

paper = '''
                                                                
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                 

      '''

scirror = '''

    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
game_images = [rock, paper, scirror]
user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_choice >= 0 or user_choice < 2:
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game_images[computer_choice]}")

if user_choice >2 or user_choice < 0:
    print("you typed an invalid number,plz enter between 0 and 1")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")

elif user_choice == computer_choice:
    print("It's a draw!")


