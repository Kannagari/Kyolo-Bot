import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import requests
import io


bot = commands.Bot(command_prefix="!")
hugMethods = ["*hugs* %s"]
WRand = ["https://www.youtube.com/watch?v=D1sZ_vwqwcE" , "https://www.youtube.com/watch?v=hgKDu5pp_fU" , "https://www.youtube.com/watch?v=HAIDqt2aUek"]
CRand = ["https://s-media-cache-ak0.pinimg.com/originals/a8/4f/16/a84f16ac8532d5a87cb0b1c931d835b9.png" , "http://img1.reactor.cc/pics/post/Anime-Boku-no-Hero-Academia-Toga-Himiko-Monochrome-%28Anime%29-3790953.png" , "http://img0.reactor.cc/pics/post/Anime-Boku-no-Hero-Academia-Toga-Himiko-makumakukawaii-3614260.jpeg" , "http://img0.reactor.cc/pics/post/Kill-la-Kill-Anime-Matoi-Ryuuko-Kiryuuin-Satsuki-3817994.jpeg" , "http://img1.reactor.cc/pics/post/Anime-New-game%21-takimoto-hifumi-3582589.jpeg" , "http://img0.reactor.cc/pics/post/Anime-Anime-Art-Hibike%21-Euphonium-Tanaka-Asuka-3997562.jpeg"]
cuteSay = ["Best Girl?" , "Hehe, almost as cute as you :3", "かわいいですね"]
SRand = ["https://media.giphy.com/media/zHGXhFJCVCbD2/giphy.gif"]
HRand = ["https://i.pinimg.com/originals/87/b5/50/87b55088247f99d5766ef6179ecdcceb.gif", "https://media.tenor.com/images/08de7ad3dcac4e10d27b2c203841a99f/tenor.gif" , "https://38.media.tumblr.com/9f6bbded87df598ea76836fbb0db8e6c/tumblr_mymyfha9TL1sm5fjzo1_500.gif" , "https://media.giphy.com/media/q3kYEKHyiU4kU/giphy.gif"]


@bot.event
async def on_ready():
    print("Logged in as: ")
    print(bot.user.name)
    print(bot.user.id)
    print("~~~~~~~~~~~")


@bot.command()
async def hai():
    await bot.say("Hai! I'm the new KyoBot~ Yoroshiku!")


@bot.command(pass_context = True)
async def echo(ctx, *, echo: str):
    await bot.delete_message(ctx.message)
    await bot.say(echo + ":revolving_hearts:")

@bot.command(pass_context = True)
async def hug(ctx, *, member : discord.Member = None):
    if member is None:
        await bot.say(ctx.message.author.mention + " there's nobody to hug ;~;")
        return
    if member.id == "292301433225609216":
        await bot.say("Awwww, I love hugs! Thanks~" + ctx.message.author.mention)
    elif member.id == "222526330514702358" and member.id == ctx.message.author.id:
        await bot.say("Awww Kyo, I'm sure someone will hug you soon~")
        sadRand = SRand[random.randrange(len(SRand))]
        response = requests.get(sadRand , stream = True)
        await bot.send_file(ctx.message.channel, io.BytesIO(response.raw.read()) , filename='image.gif' , content = '')
    elif member.id == ctx.message.author.id:
        await bot.say("Will somebody please hug " + ctx.message.author.mention + " so they aren't lonely~")
    else:
        random.seed(time.time())
        chosenResp = hugMethods[random.randrange(len(hugMethods))] % member.mention
        await bot.say(ctx.message.author.mention + " " + chosenResp)
        HugRand = HRand[random.randrange(len(HRand))]
        response = requests.get(HugRand, stream = True)
        await bot.send_file(ctx.message.channel, io.BytesIO(response.raw.read()) , filename='image.gif' , content = '')
   
@bot.command(pass_context = True)
async def choice(ctx, *, choices: str):
    choicesArr = choices.split(",")
    chosen = choicesArr[random.randrange(len(choicesArr))]
    await bot.say(ctx.message.author.mention + " I choose: `" + chosen + "`")

   
@bot.command(pass_context = True)
async def Worlds(ctx, *, member : discord.Member = None):
    worldsRand = WRand[random.randrange(len(WRand))]
    await bot.say(ctx.message.author.mention + " 【=◈︿◈=】")
    await bot.say(worldsRand)

@bot.command(pass_context = True)
async def cute(ctx):
    cuteRand = CRand[random.randrange(len(CRand))]
    csRand = cuteSay[random.randrange(len(cuteSay))]
    response = requests.get(cuteRand , stream=True)
    await bot.send_file(ctx.message.channel, io.BytesIO(response.raw.read()) , filename='image.png' , content = csRand)
       
