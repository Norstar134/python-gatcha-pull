import os
import time
import pandas as pd
from menus import main_menu, banner_menu, character_menu, banner_pull_menu
from data_transformation import extract_data_limited_zzz, add_data_limited_zzz

clear = lambda: os.system('cls')

while True:
    print(main_menu())
    user_input = input("> ")

    try:
        user_input = int(user_input)
        if (user_input == 0):
            break

        elif (user_input == 1):
            while True:
                print(character_menu())
                user_input = input("> ")
                try:
                    user_input = int(user_input)
                    if (user_input == 0):
                        break

                    elif (user_input == 1):
                        df_limited = extract_data_limited_zzz("../csv_files/limited_characters_zenless_zone_zero.csv")
                        print(df_limited.to_string())
                    
                    elif (user_input == 2):
                        add_data_limited_zzz("../csv_files/limited_characters_zenless_zone_zero.csv")

                except Exception as err:
                    print(f"Sorry! We've run into a problem: {err}")
        
        elif (user_input == 2):
            while True:
                print(banner_menu())
                user_input = input("> ")
                if (user_input == 0):
                    break
        
        elif (user_input == 3):
            while True:
                print(banner_pull_menu())
                user_input = input("> ")
                if (user_input == 0):
                    break
    
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")