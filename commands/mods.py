import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions


class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members = True)
    async def kick(self, ctx, member:Member, *, reasons=None):
        await member.kick(reason=reasons)
        await ctx.send(f"{member} got kicked because of {reasons}")



    @commands.command()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member:Member, *, reasons=None):
        await member.ban(reason=reasons)
        await ctx.send(f"{member} got banned because of {reasons}")


async def setup(bot):
    await bot.add_cog(Mods(bot))