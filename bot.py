import discord
from discord.ext import commands
import json
import random

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
    keyword_dict = {
        "bbbb87cry": jdata["bbbb87cry"],
        "nlnlsofun": jdata["nlnlsofun"],
        "D:": jdata["D:"],
        "nlnlouo": jdata["nlnlouo"],
        "俊宏愛你": jdata["俊宏愛你"],
        "累了": jdata["累了"],
        "舔舔": jdata["舔舔"],
        "...": jdata["..."],
        "aquasmoke": jdata["aquasmoke"],
        "讚": jdata["讚"],
        "penis good": jdata["penis good"]
    }

    greetings = ["你好", "哈囉", "安安"]

    pic = None
    for keyword in keyword_dict:
        if keyword in msg.content:
            pic = discord.File(keyword_dict[keyword])
            break
    
    if any(keyword in msg.content for keyword in greetings) and msg.author!=bot.user:
        greeting = random.choice(greetings)
        await msg.channel.send(f"{msg.author.mention} {greeting}!")
    elif "原神" in msg.content and msg.author!=bot.user:
        user = discord.utils.get(msg.guild.members, name="iantang")
        await msg.channel.send(f"{user.mention}不要再玩原神了")
    elif any(keyword in msg.content for keyword in ["日麻", "雀魂"]) and msg.author!=bot.user:
        await msg.channel.send("@everyone 該搓日麻了吧!")

    if pic:
        await msg.channel.send(file=pic)


bot.run(jdata["TOKEN"])
