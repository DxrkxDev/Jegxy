import discord
from discord.ext import commands
from discord.ext.commands.core import command

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("bot is online!")

@client.command()
async def ping(ctx):
    await ctx.send('pong')


client.run('ODgyNDM1ODAyMDkxNjI2NTE3.YS7WYg.IezByd2yaDcPtYfvlDMsRFFe_7I')