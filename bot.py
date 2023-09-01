import discord
import os
from words import *
from datetime import datetime
from discord.ext import commands

now = datetime.now()

bot = commands.Bot(command_prefix="?",intents=discord.Intents.all())
extensions = []

@bot.event
async def on_ready():
    print("The bot is ready!")
    for extension in extensions:
        await bot.load_extension(extension)
        

@bot.event
async def on_message(msg):
    await bot.process_commands(msg)
    automod_embed = discord.Embed(
        title="AutoMod",
        description=f"{msg.author}, stop swearing!",
        colour=discord.Color.red()
    )
    for word in blacklisted_words:
        if word in msg.content.lower() and msg.author.id != bot.user.id:
            await msg.channel.send(embed=automod_embed)
            await msg.delete()

    
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        extensions.append("commands."+filename[:-3])

print(extensions)

bot.run("TOKEN")