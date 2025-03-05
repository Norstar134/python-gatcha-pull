import pandas as pd

def extract_data_limited_zzz(filename):
    df = pd.read_csv(
        filename,
        header=None,
        skiprows=1,
        names=["character_name","character_rank","character_attribute","character_specialty","faction","gatcha_banner","versions","pull_amount"]
    )

    return df

def add_data_limited_zzz(filename):
    new_character = {}
    character_name = input("Please type in the character's name > ")
    new_character["character_name"] = character_name
    character_rank = input("Please type in the character rank > ")
    new_character["character_rank"] = character_rank
    character_attribute = input("Please type in the character attribute > ")
    new_character["character_attribute"] = character_attribute
    character_specialty = input("Please type in the character specialty > ")
    new_character["character_specialty"] = character_specialty
    character_faction = input("Please type in the character faction > ")
    new_character["faction"] = character_faction
    character_banner = input("Please type in the character banner name > ")
    new_character["gatcha_banner"] = character_banner
    character_versions = input("Please type in the patches the character can be pulled, commas can be used if they have appeared multiple times > ")
    new_character["versions"] = character_versions
    character_pulls = 0
    new_character["pull_amount"] = character_pulls

    df = pd.DataFrame([new_character])
    with open(filename, 'a') as f:
        df.to_csv(f, index=False, header=False, mode="a")

    df_read = extract_data_limited_zzz(filename)

    return df_read