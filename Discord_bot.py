import discord
import requests
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def nasilsin(ctx):
    await ctx.send(f"iyiyim sen nasılsın")




@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def uygulama(ctx):
    mesaj = """İşte çevre kirliliği hakkında bilgi veren bazı uygulamalar:

- **Ulusal Hava Kalitesi İzleme Ağı**: Hava kirliliği seviyelerini takip eder ve hava kalitesi hakkında bilgi verir.
- **Forest**: Telefon kullanımını sınırlayarak sanal ağaçlar büyütür ve gerçek ağaç dikimine katkı sağlar.
- **Earth Hero**: Kişisel karbon ayak izinizi hesaplar ve azaltmak için eylemler önerir.
- **Pirika**: Çöpleri toplar ve çevre temizliğine katkı sağlar.
- **Dijital Kadıköy**: Çevre kirliliği ve geri dönüşüm gibi konularda bilgilendirme yapar.

Bu uygulamalar çevre bilincini artırmak ve sürdürülebilir bir yaşam tarzı benimsemek için kullanışlıdır.
"""
    await ctx.send(mesaj)
    
@bot.command()
async def doğada_yokolma_süreci(ctx,*,item: str):
    yok_olma_süresi= {
        "plastik şişe": "450-500 yıl",
        "cam şişe": " 1milyon yıl",
        "kağıt": "1 ay",
        "metal kutu": "50-60 yıl",
        "konserve kutu": "500 yıl",
        "plastik poşet": "1000+ yıl",
        "süt kutuları": "250-300 yıl",
        "piller": "100 yıl"
    }
    await ctx.send(yok_olma_süresi.get(item.lower(), "Bu eşya için elimde veri yok."))
