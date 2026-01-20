'''
DAY 4: Starting to create a Discord bot
Today I Learned a lot of things about Python by trying to create my first bot on Discord, I already tried something similar with Luau but this is much different
With Python, there are a lot of useful commands that I would never have thought with Luau
Let's see what we can make this bot doing:
'''

import discord # Before this I installed an API for Discord, then I can import that
from discord.ext import commands

#PERMISSIONS
intents = discord.Intents.default()
intents.message_content = True # The bot can now see the context of my messages
intents.members = True # Now the bot can see if there's a new member, if someone left the server, etc...

#CREATING A PREFIX FOR COMMANDS (THAT THE BOT WILL RESPOND TO)
bot = commands.Bot(command_prefix="!", intents=intents)

#ON.READY() EVENT
@bot.event
async def on_ready():
    print("--------BOT ONLINE--------")
    print(f"logged as: {bot.user}")
    print("--------------------------") # Small function executed when the bot is online

#HELLO COMMAND
@bot.command()
async def hello(ctx):
    await ctx.send(f"Greatings {ctx.author.mention}, everything works good!") # Command executed when someone says "!hello"


bot.run("YOUR_TOKEN_HERE") # This logs in the bot

'''
I learned a lot of things today, but can't put everything now so I'm dividing days dedicated to the Discord bot between weeks, so my brain doesn't go boom
'''