import discord
from discord.ext import commands
import json

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="*", intents=intents) #建置實體Bot,(command_prefix指令前綴,intents設定)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["WELCOME_CHANNEL"]))
    await channel.send(f"{member} 加入了秘密基地!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["LEAVE_CHANNEL"]))
    await channel.send(f"{member} 888888!")

@bot.command()
async def ping(ctx):                                #ctx(上下文)，回覆上下文所在的頻道
    await ctx.send(f"{round(bot.latency*1000)} (ms)")

@bot.event
async def on_message(msg):
    if msg.content == "bbbb87cry" :
        pic = discord.File(jdata["bbbb87cry"])
    elif msg.content == "nlnlsofun" :
        pic = discord.File(jdata["nlnlsofun"])
    elif msg.content == "D:" :
        pic = discord.File(jdata["D:"])
    elif msg.content == "nlnlouo" :
        pic = discord.File(jdata["nlnlouo"])
    await msg.channel.send(file=pic)

bot.run(jdata["TOKEN"])
