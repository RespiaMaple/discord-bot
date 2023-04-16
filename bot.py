import discord
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="/", intents=intents) #建置實體Bot,(command_prefix指令前綴)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

bot.run("MTA5NzE3NDQwMzQxMTg3ODA0MQ.Gncg0B.mf0x-7PYljQpsN3P42QTo2yqOa2cX0bxN8jozM")
