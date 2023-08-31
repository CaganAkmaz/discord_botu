import discord
from bot_mantik import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sunucuya başarılı bir şekilde giriş yapıldı, Çağan bey.')

@client.event
async def on_message(message):
    
    
    if message.author == client.user:
        return
    if message.content.startswith('Merhaba'):
        await message.channel.send("Hoş Geldin!")
    elif message.content.startswith('Şifre'):
        await message.channel.send(sifre_uret(10))
    elif message.content.startswith('görüşürüz'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('emoji'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('para'):
        await message.channel.send(yazi_tura())
    else:
        await message.channel.send("Bu komutu anlayamadım :(")
    

client.run("MTE0NTMwMTcxODUzNjU3Mjk0OA.GLpCXn.iXOB1Tdl02253qj7ySYfIXr8fbA3cmhgWgEuH0")