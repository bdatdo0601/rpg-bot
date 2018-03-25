import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json
import io
import os

game_status = 0
Client = discord.Client()
client = commands.Bot(command_prefix = "")

async def handleStart(message):
    if (game_status == 0):
        await client.send_message(message.channel, "Participant players type 'entering'")
        global game_status
        game_status = 1

    elif (game_status == 1):
        await client.send_message(message.channel, "Game initialization already in progress")

async def addPlayers(message):
    if(game_status==-1):
        await client.send_message(message.channel, "Game in progress")
    if(game_status==0):
        await client.send_message(message.channel, "No active game")
    elif(game_status==1):
        with open('player_list','r+') as f:
            json_data = json.load(f)
            json_data['%s',message.author] = "True"
            f.seek(0)
            f.write(json.dumps(json_data))
            f.truncate()

async def beginGame(message)

async def handleLeaveGame(message):
    if (game_status == 0):
        await client.send_message(message.channel, "No active game")
    else:
        await client.send_message(message.channel, "Player has left the game lobby")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "!Start game":
        await handleStart(message)

    elif message.content == "!entering":
        await addPlayers(message)

    elif message.content == "!Begin game":
        await handleBegin(message)

    elif message.content == "!Exit lobby":
       await handleLeaveGame(message)



client.run("NDI3MTY0NjM4MDA2NzM4OTY1.DZg8uQ.v9tarVkSpDBMpJ6uJmL3MrfKXPE")