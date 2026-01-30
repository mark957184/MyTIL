'''
DAY 10: JSON files
Today I Learned a way to save data permanently on a file JSON, so even though the py file is closed or the pc is turned off, all data is still accessible and not erased as usual:
'''

import json

data = {
    "player_list": ["Mark", "bot", "bot1", "bot2"],
    "maps": 19,
    "gamemodes": ["1V1", "2V2", "3V3", "5V5", "zombies"],
    "rounds_duration": 180
}

save_file = "data.json"

with open(save_file, "w") as f:
    json.dump(data, f, indent=4)
    print(f"Data saved in: {save_file}")

print("------------------------------------------------------------------")

'''
Here is a code I made to save data in a JSON file:
'''

save_file = "rubric.json" # BE aware of the file path

try:
    with open(save_file, "r") as f:
        rubric = json.load(f)
        print(f"Data loaded from rubric: {save_file}")
except FileNotFoundError:
    with open(save_file, "w") as f:
        rubric = {}
        json.dump(rubric, f, indent=4)
        print(f"No existing rubric found. Created new rubric: {save_file}")

while True:
    rubric_list = ""
    for i in rubric:
        l = list(rubric.keys())
        index = l.index(i)
        if index >= 1:
            rubric_list += ", "
        rubric_list = rubric_list + f"{i} ({rubric[i]})"
    print(f"\nCurrent rubric: {rubric_list}")
    action = input("Would you like to add a new contact? (name:phone number or type 'exit' to quit): ")
    if action == 'exit':
        break
    if ':' in action:
        name, phone = action.split(':')
        rubric[name] = phone
        with open(save_file, "w") as f:
            json.dump(rubric, f, indent=4)
        print(f"Added {name}: {phone}")
    else:
        print("Invalid format. Please use 'name:phone number'!")


'''
This code allows you to create a simple contact list (rubric) that is saved in a JSON file. You can add new contacts, and the data will persist even after closing the program!
'''