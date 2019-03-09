import sqlite3
import discord
from discord.ext import commands
import asyncio
from os import getcwd
import json
from io import BytesIO

class Special():
    def __init__(self, client):
        self.client = client
        self.lastseen = ""

    def getid(self, name):
        with open(getcwd().replace("DisBot","pokemon.json"),"r") as f:
            data = json.load(f)
            f.close()
        for i in data:
            if data[i]["name"].lower().strip() == name.lower().strip():
                return i
        return 1

    async def on_message(self, message):
        if message.author.id == "365975655608745985":
            self.lastseen = message
        if message.author.id == "544450644015185940":
            if message.embeds != [] and message.embeds[0]["title"].startswith("Possible Pokemon"):
                chanid = "553855431513210880"
                channel = self.client.get_channel(chanid)
                roleid = "530696857450577920"
                pokename = message.embeds[0]["title"].split(":")[1].lower().strip()
                dex = self.getid(pokename)
                namelist = ["articuno", "zapdos", "moltres", "mewtwo", "mew", "raikou", "entei", "suicune", "lugia", "ho-oh", "celebi", "regirock", "regice", "registeel", "latias", "latios", "kyogre", "groudon", "rayquaza", "jirachi", "deoxys", "uxie", "mesprit", "azelf", "dialga", "palkia", "heatran", "regigigas", "giratina", "cresselia", "darkrai", "phione", "manaphy", "shaymin", "arceus", "victini", "cobalion", "terrakion", "virizion", "tornadus", "thundurus", "zekrom", "reshiram", "landorus", "kyurem", "keldeo", "meloetta", "genesect", "xerneas", "yveltal", "zygarde", "diancie", "hoopa", "volcanion", "tapu koko", "tapu lele", "tapu fini", "tapu bulu", "cosmog", "cosmoem", "solgaleo", "lunala", "necrozma", "magearna", "marshadow", "beldum", "metang", "metagross", "nihilego", "buzzwole", "pheromosa", "xurkitree", "celesteela", "kartana", "guzzlord", "poipole", "naganadel", "stakataka", "blacephalon", "type: null", "silvally", "zeraora", "meltan", "melmetal"]
                if pokename in namelist:
                    img_dir = getcwd().replace("DisBot", "artwork") + "/" + str(dex) + ".png"
                    with open(img_dir, 'rb') as f:
                        buffer = BytesIO(f.read())
                    e = self.lastseen.embeds[0]
                    e['image']['url'] = "attachment://PokecordSpawn.png"
                    data = await self.client.http.send_file(channel.id, buffer, guild_id=channel.server.id,
                                                            filename='PokecordSpawn.png',
                                                            embed=e)
                    m1 = self.client.connection._create_message(channel=channel, **data)
                    m2 = await self.client.send_message(channel,"**In** "+message.channel.mention)
                    await self.client.add_reaction(m1, "a:DiscordHype:535081629065019402")
                    await self.client.send_message(message.channel, "<@&"+str(roleid)+"> A rare Pokemon has just spawned here! Good luck catching it!")
                    await self.client.pin_message(self.lastseen)


def setup(client):
    client.add_cog(Special(client))

