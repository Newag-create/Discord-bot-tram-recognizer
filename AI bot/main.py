import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    channel = bot.get_channel(1498365960153989284)  # ID kanału
    
    if channel:
        await channel.send(
            f'Cześć👋, jestem {bot.user}!\n'
            'PL Jeśli chcesz sklasyfikować jakiś model tramwaju🚋 to wyślij mi jego zdjęcie i napisz $check. '
            'A jeżeli chcesz zapisać jakiś obraz🌅 to wyślij go📨 i napisz $save. '
            'EN If you want to classify a tram model🚋, send me its photo and type $check. ' 
            'And if you want to save an image🌅, send it📨 and type $save.')

@bot.command()
async def save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename  # noqa: F841
            file_url = attachment.url  # noqa: F841
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Zapisano obraz w ./{attachment.filename}")
    else:
        await ctx.send("Zapomniałeś załadować obraz :(")
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename  # noqa: F841
            file_url = attachment.url  # noqa: F841
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(
                get_class(
                    model_path="./keras_model.h5",
                    labels_path="labels.txt",
                    image_path=f"./{attachment.filename}",
                )
            )
    else:
        await ctx.send("Zapomniałeś załadować obraz :(")

bot.run("TOKEN")
