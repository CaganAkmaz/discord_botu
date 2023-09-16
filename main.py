import discord
from discord.ext import commands

import random
import os

kati_atik_liste = ["İçeceklerinizi tek kullanımlık plastik şişelerde satın almak yerine, geri dönüştürülebilir ürünleri tercih edebilirsiniz.",
                   "Satın alımlarınızı azaltın: Ne kadar az şey alırsanız, o kadar az çöp üretirsiniz.", 
                   "Ürünleri yeniden kullanmak atığınızı azaltır, para tasarrufunuzu artırarak doğal kaynakları korumaya da yardımcı olur.", 
                   "Çevrenin korunmasına yardımcı olmak için geri dönüştürülmüş materyallere yatırım yapın, onları satın alın.", 
                   "Temizlik ürünleri kullanımının yarattığı atığa katkı yapmak yerine, sirke ve karbonat gibi doğal, çevre dostu temizlik ürünlerini kullanın.", 
                   "Geri dönüşüm yapın. Geri dönüşüm yapmak önceden kullanılan materyallere ikinci bir hayat verir, dolayısıyla atıkların azaltılmasına ciddi katkıda bulunur.", 
                   "Organik gübre yaratın. Bahçe ve yiyecek atıkları gibi organik atıklar, toplam atığın %25 ila %50’si arasındaki bir miktarını oluşturuyor. Bunun tamamını organik gübreye dönüştüremeyebilirsiniz, ancak bir kısmını gübre olarak kullanmak bile atık miktarınızı azaltır.",
                   "Mahallenizdeki diğer insanlarla iletişim kurun, katı atık miktarınızı azaltmanın avantajlarını konuşun. Topluluğunuzdaki atıklar ve uygulanan geri dönüşüm politikaları hakkında daha fazla bilgi alın.", 
                   "Sizin davranışlarınız başkalarına da örnek olabilir. İnsanlar, bir fark yaratabildiğinizi görürlerse, başarılarınızı tekrarlamak isteyebilirler."]

mesaj = "Sunucuya hoş geldin"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def mem(ctx):
    fname = random.choice(os.listdir('images'))
    with open(f'images/{fname}', 'rb') as f:
    
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def katı_atık(ctx):
    bilgi = random.choice(kati_atik_liste)
    await ctx.send(bilgi)


@bot.event
async def on_member_join(member):
    await member.send(mesaj)


@bot.command()
async def yardım(ctx):
    await ctx.send("Hoş Geldin! !mem yazarak rastgele memlerimizden birisini görebilirsin!   !merhaba yazarak benden bir selam alabilirsin.  !heh yazarak benimle gülüşebilirsin.  !katı_atık yazarak katı atıklarımızı nasıl azaltıp çevreye karşı daha duyarlı olabileceğimiz hakkında rastgele bilgilerimizden birisini öğrenebilirsin. ")


@bot.command()
async def kick(ctx, member: discord.Member, *, sebep):
    await member.kick(reason= sebep)
    await ctx.send(f"**{member.mention}**, **{sebep}** sebebiyle sunucudan atıldı!")


@bot.command()
async def ban(ctx, member: discord.Member, *, sebep):
    await member.ban(reason= sebep)
    await ctx.send(f"**{member.mention}**, **{sebep}** sebebiyle sunucudan yasaklandı!")




bot.run("token")
