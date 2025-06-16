import discord
from discord.ext import commands
from googlesearch import search  
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("Bot is running!")

@client.command()
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention}, what would you like to search for?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await client.wait_for('message', timeout=30.0, check=check)
        query = f'"{msg.content}" filetype:pdf OR filetype:xlsx OR filetype:docx'
        await ctx.send("Searching...")

        results = []
        for url in search(query, num_results=5):
            results.append(url)
        await ctx.send(query)
        if results:
            for i, url in enumerate(results, 1):
                await ctx.send(f"{i}. {url}")

        else:
            await ctx.send("No results found.")
    except asyncio.TimeoutError:
        await ctx.send("You didn't respond in time!")


client.run('key')
