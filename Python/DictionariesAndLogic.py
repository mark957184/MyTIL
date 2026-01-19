'''
DAY 3: Dictionaries and logic
Back to learning! Today I Learned about dictionaries, very important for logic cycles and for storing data
Not just by the value as in lists, but with a key
Let's see an example:
'''

player = {
    "name": "Mark",
    "inventory": ["sword","shield","boots","chestplate","healthPotion"],
    "HealthPotionInInventory": True,
    "HealthPotionUsable": False,
    "HP": 100,
    "AP": 50
}

'''
As you can see you can store a list inside a dictionary (storing efficiency squared!)
Let's try something a little bit harder, let's print something when the player's HP is decreasing
To do that, we'll use a 'if' to make different things happen based on a sentence, here an example:
'''

if player["HP"] < 100:
    print("Ouch!")

# Now I want to try something, lowering the health, printing a message, be able to use a health potion, use it, removing it from the inventory and healing:

player["HP"] -= 40

if player["HP"] < 100:
    player["HealthPotionUsable"] = True
    print("Ouch!")

# Here it's better to use a function but it would be better not rushing things

if player["HealthPotionUsable"] == True and player["HealthPotionInInventory"] == True:
    player["HP"] += 40

    player["HealthPotionUsable"] = False
    player["HealthPotionInInventory"] = False

    i = player["inventory"].index("healthPotion")
    del player["inventory"][i]

    print("Aaah! I feel better!")

'''
Got it! Python it's more similar to Luau than I thought! I guess I can make things faster
Let's see another cycle, the 'for' cycle:
'''

numbers = [1, 2, 3, 4, 5, 6, 7]

for n in numbers:
    print("this should be seen 7 times")

# Now the 'While' cycle, it executes one or more commands while a sentence is true, let's see it here:

while not player["HP"] == 100:
    player["HealthPotionUsable"] = True

'''
For today that's all, tomorrow i'll start with some logic and cycles exercises
I know that this may seem like a tutorial for beginners instead of a TIL but (as a Luau developer) the first lessons in Python hadn't had a lot of TIL things, but I decided to put everything here so...
Can't wait to learn new things tomorrow!
'''