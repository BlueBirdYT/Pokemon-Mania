import sqlite3
import discord
from discord.ext import commands
import asyncio

class Short():
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.author.id == "365975655608745985":
            if message.embeds is not []:
                emc = message.embeds[0]
                if "author" in emc and emc['author']['name'] == "Professor Oak":
                    try:
                        await self.client.delete_message(message)
                    except Exception as e:
                        print(e)
                    extext = ""
                    if "fields" in emc and len(emc["fields"]) >= 1:
                        extext = "\n\n"+emc["fields"][0]["value"]
                    e = discord.Embed(title=emc['title'], description=emc['description']+extext,
                                      color=discord.Color(0x00ff00))
                    e.set_thumbnail(url=emc['image']['url'])
                    if "footer" in emc: e.set_footer(text=emc['footer']['text'])
                    await self.client.send_message(message.channel, embed=e)


def setup(client):
    client.add_cog(Short(client))