import random
from config import ans4
from config import ans3
from config import XP_step
from config import max_level

class Player():
    def __init__(self, player_name, XP, level):
        self.player_name = player_name
        self.XP = XP
        self.level = level

    def earn_XP(self):
        self.XP += XP_step
        print(f"{self.player_name} earned {XP_step} XP!")

    def level_up(self):
        self.XP = 0
        self.level += 1
        ans = random.choice(ans4)
        print(f"{self.player_name} {ans}")
    

p = input("What's your username? ")
player = Player(p, 0, 1)

def login():
    print(f"-------------Welcome back, {player.player_name}!-------------")
    print(f" XP: {player.XP}")
    print(f" Level: {player.level}")
    print("---------------------------------------------")
    ans1 = random.choice(ans3)
    e = input(ans1)
    if e == "e":
        if player.level < 5:
            player.earn_XP()
            if player.XP == 100:
                player.level_up()
            return
        else:
            print("Max level reached!")
            return
    else:
        return

while True:
    login()