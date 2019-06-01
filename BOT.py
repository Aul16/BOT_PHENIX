import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print("Connected")

bot.remove_command('help')
@bot.command()
async def help(ctx):
	await ctx.author.send("Commandes pour avoir des conseils sur certains héros: ![nom du héros] (exemple: !zenyatta)")

@bot.command()
async def inscription(ctx):
    await ctx.send("https://docs.google.com/forms/d/1jcEg6qXygwpeWs0n5ctkTx-GW9wgI0r-P7dNhQrzc54")

@bot.command()
async def ana(ctx):
    await ctx.send("Conseil(s):  Ne restez pas h24 dans votre viseur ca peux vous encombrer "
    	"la vue et vous faire perdre un team fight, priorisez le tir sans lunette si vous êtes encore débutant \n"
                   "https://www.youtube.com/watch?v=ifINpdZzw4s \n"
                   "https://www.youtube.com/watch?v=5Ex_yJQ8Opg&")

@bot.command()
async def ange(ctx):
    await ctx.send("Conseil(s): utilisez la technique donnée dans la vidéo " 
    	"ci-dessous et n'hésitez pas a en abuser \n"
    	"https://www.youtube.com/watch?v=-fhuiZwhG0o&")

@bot.command()
async def baptiste(ctx):
    await ctx.send("Conseil(s): le champs d'immortalité peux très bien être utilisé de loin, " 
    	"il faut juste savoir où les lancer un peux comme une grenade d'ana donc si vos alliés "
    	"sont sur le point et que vous êtes mort, n'hésitez pas à le lancer de loin, ca évitera à vos alliés de mourir \n"
    	"https://www.youtube.com/watch?v=fkM6nbxvchk")

@bot.command()
async def brigitte(ctx):
    await ctx.send("Conseil(s): utilisez votre ulti avec votre shield levé, ca vous évitera de vous prendre un head shot \n"
    	"https://www.youtube.com/watch?v=Q5i2Ive8B3M")

@bot.command()
async def moira(ctx):
    await ctx.send("Conseil(s): si vous n'avez plus de heal, faites des petits coups de tir principal non "
    	"continues (exemple: spam votre click gauche), ca vous rechargera plus vite \n"
    	"https://www.youtube.com/watch?v=IikjcyVIJIw& \n"
    	"https://www.youtube.com/watch?v=te1vV4F6YDQ")

@bot.command()
async def lucio(ctx):
    await ctx.send("Conseil(s): n'hésitez pas à aller dans le back de l'ennemie pour boop le reinhardt adverse (en goat ) \n"
    	"https://www.youtube.com/watch?v=4A64G7CeeZY \n"
    	"https://www.youtube.com/watch?v=8vTb5G5Mh0c")

@bot.command()
async def zenyatta(ctx):
    await ctx.send("Conseil(s): la visée de zenyatta est très dure à apprendre donc si vous ne savez pas viser avec "
    	"celui-ci, essayez de mettre quelques tir dans la mêlée, vous toucherez une fois sur deux \n"
    	"https://www.youtube.com/watch?v=vZAkzlPPx8I&")


bot.run("NTgzOTMzMjI4MDA4NzM0NzIw.XPKA2g.W9Rfaz4m2V2Jz-RcMIB09JqyTGE")
