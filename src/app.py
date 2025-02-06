import os
import time
from menus import main_menu, banner_menu, character_menu, banner_pull_menu

clear = lambda: os.system('cls')

while True:
    print(main_menu)
    user_input = input("> ")

    try:
        user_input = int(user_input)
        if (user_input == 0):
            break

        elif (user_input == 1):
            print(character_menu)
        
        elif (user_input == 2):
            print(banner_menu)
        
        elif (user_input == 3):
            print(banner_pull_menu)
    
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")