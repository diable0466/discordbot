import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'로그인 완료: {bot.user}')

@bot.command()
async def 안녕(ctx):
    await ctx.send('안녕! 나는 항상 깨어있는 봇이야! 😊')

bot.run(os.environ['TOKEN'])
