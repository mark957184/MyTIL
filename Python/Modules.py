'''
DAY 6: Modules
Today I Learned about modules, that consists in creating more files so you can save some functions, dictionaries, classes, etc... in, for example, a 'config.py' file, so the code in the main file (main.py usually) is cleaner
It's used to separate code to make it easier to debug too
Here some code I made (with the class I made yesterday as config.py file):
'''

import Functions # This imports everything from the file, PS: I wrote import 'Functions' because the name of the file was 'Functions'

from Functions import BotConfig # In this way I imported just the class 'BotConfig' inside 'Functions' file

bot1 = BotConfig("PyBot", "1.2.5", "Mark")
bot1.get_info()

'''
There are some default modules in Python always accessible, such as 'random' or 'os':
'''

import random

opt = ["Yes", "No", "Maybe"]
ans = random.choice(opt)
print(f"The bot says: {ans}")

'''
I don't have much time for Python today, tomorrow maybe I'll do something more to keep up!
'''