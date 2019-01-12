# Import so that the bot could function
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
from random import randint
import Config
import datetime
import asyncio
import discord
from discord.ext.commands import Bot

#Determine the bots prefix
bot = commands.Bot(command_prefix = Config.PREFIX)

@bot.event
async def on_ready():
    print("===================================")
    print("Logged in as: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print('Server count:', str(len(bot.servers)))
    print('User Count:',len(set(bot.get_all_members())))
    print("Py Lib Version: %s"%discord.__version__)
    print("===================================")

@bot.command(pass_context = True)
async def rules(ctx):
		embed = discord.Embed(title="Welcome To The Official SkiGang Discord Server!", colour=discord.Colour(0xea821a), timestamp=datetime.datetime.utcfromtimestamp(1547283256))

		embed.set_thumbnail(url="https://i.imgur.com/hYceQ6F.jpg")

		embed.add_field(name="Rules", value="1. Do NOT Spam Music unless allowed, or in a music only channel.")
		embed.add_field(name="\u200B", value="2. Do NOT impersonate anyone.")
		embed.add_field(name="\u200B", value="3. Do NOT spam any chats.", inline = False)
		embed.add_field(name="\u200B", value="4. No trolling, at least keep it to a minimum :wink:")
		embed.add_field(name="\u200B", value="5. No Channel hopping. Channel hopping is defined as switching channels in quick succession for either positive or negative purposes.")
		embed.add_field(name="\u200B", value="6. No glitching of any kind, or attempting to gain control of permissions through dishonest means.")
		embed.add_field(name="\u200B", value="7. No Innappropriate pictures/porn pics in any chat other than #nsfw-ðŸ’€")
		embed.add_field(name="\u200B", value="8. Be respectful to all users/staff.")
		embed.add_field(name="\u200B", value="9. No spamming staff for roles/ranks.")
		embed.add_field(name="\u200B", value="10. Have a fun time and enjoy your stay!")
		embed.add_field(name="\u200B", value="\u200B")
		embed.add_field(name="\u200B", value="\u200B")
		embed.add_field(name="\u200B", value="\u200B")
		embed.add_field(name = "------------Support Rules/HowTo------------", value = "If you have any questions about the discord server or about your Garry's Mod server please see the #support-ðŸŽ« channel and use the command -new YOURQUESTION", inline = False)
		embed.add_field(name = "\u200B", value = "DO NOT ASK FOR SUPPORT IN GENERAL CHAT... ONLY #support-ðŸŽ« CHAT", inline = True)
		embed.add_field(name = "--------------------END--------------------", value = "\u200B", inline = True)
		embed.add_field(name="\u200B", value="\u200B")
		embed.add_field(name="\u200B", value="\u200B")

		await bot.say(content="", embed=embed)
		
@bot.command(pass_context = True)
async def support(ctx):
		embed = discord.Embed(title="Discord Support HowTo", colour=discord.Colour(0xea821a), timestamp=datetime.datetime.utcfromtimestamp(1547283256))

		embed.set_thumbnail(url="https://i.imgur.com/hYceQ6F.jpg")
		
		embed.add_field(name="Commands", value="To create a ticket please use the command -new YOURQUESTION")
		embed.add_field(name="Please give all support staff time to read and respond to each problem/question thanks.", value="\u200B")

		await bot.say(content="", embed=embed)
    
bot.run(Config.TOKEN)
