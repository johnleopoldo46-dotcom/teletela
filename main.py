import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Teletela Central conectada como {bot.user}")

@bot.command(name="vigiar")
async def vigiar(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("- Teletela ativada. O Partido observa.")
    else:
        await ctx.send("- Erro: Cidadão fora do canal de voz.")

# Pega o token direto daquela variável DISCORD_TOKEN que você criou no Railway
bot.run(os.getenv("DISCORD_TOKEN"))
