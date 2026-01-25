'''
DAY 8: Error handling
Today I learned how to handle possible situations where you could get errors using try and except:
'''

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv(r"C:\Users\USER\OneDrive\Desktop\NON APRIRE\[REDACTED]\ProjectIT\Month 1\Python\tokenId.env") # Don't mind this, just the directory where I put the .env file 

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def dividing(ctx, a: int, b: int):
    try:
        result = a / b
        await ctx.send(f"The result is {result}")
    except ZeroDivisionError:
        await ctx.send(f"Can't divide by zero!")
    except Exception as e:
        await ctx.send(f"Something went wrong: {e}")

bot.run(os.getenv("TOKEN_ID"))

'''
This example is perfect with almost everything where you could get errors, handling those and executing something else
'''