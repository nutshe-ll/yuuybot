import discord
import random
import sys
from datetime import datetime
from discord.ext import commands


sys.path.insert(0, "C://Users//Hugo//Downloads//file")
from words import *


now = datetime.now()



class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def rps(self, ctx, user_choice: str=None):
        choices = ["rock", "paper", "scissors"]
        player = None
        if user_choice != None:
            player = user_choice.lower()
        bot = random.choice(choices)

        dt_string = now.strftime(f"%H:%M:%S, %B/%d/%Y")
        print(dt_string)
        
        embed = discord.Embed(
            colour=discord.Colour.red(),
            description="",
            title="[RPS] Rock Paper Scissors"
        )

        embed.set_footer(text=dt_string)
        embed.set_author(name=f"{ctx.author.name}")

        if player == bot:
            embed.description = f"*Bot: **{bot}***\n*You chose: **{player}***\n\n**You tied!**"
            await ctx.send(embed=embed)

        elif player == "rock":
            if bot == "scissors":
                embed.description = f"*Bot: **{bot}***\n*You chose: **{player}***\n\n**You win!**"
                await ctx.send(embed=embed)
            elif bot == "paper":
                embed.description = f"*Bot: **{bot}***\n*You chose: **{player}***\n\n**You lose!**"
                await ctx.send(embed=embed)

        elif player == "paper":
            if bot == "rock":
                embed.description = f"*Bot: **{bot}***\n*You chose: **{player}***\n\n**You win!**"
                await ctx.send(embed=embed)
            elif bot == "scissors":
                embed.description = f"*Bot: **{bot}***\n*You chose: **{player}***\n\n**You lose!**"
                await ctx.send(embed=embed)
            
        elif player == "scissors":
            if bot == "paper":
                embed.description = f"*Bot: **{bot}***\n*You chose: **{player}***\n\n**You win!**"
                await ctx.send(embed=embed)
            elif bot == "rock":
                embed.description = f"*Bot: **{bot}***\n*You chose: **{player}***\n\n**You lose!**"
                await ctx.send(embed=embed)
        elif user_choice == None:
            await ctx.send("Enter an argument to start the game! Gimana sih rek :joy:.")
        else:
            await ctx.send(f"Sorry, **{player}** is not a valid argument :joy:, wailah rek! (Rock, Paper Scissors)")


    @commands.command()
    async def homok(self, ctx):
        homok_word = random.choice(jokes_homok)
        await ctx.send(homok_word)


async def setup(bot):
    await bot.add_cog(Fun(bot))