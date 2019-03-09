from discord.ext import commands
from discord import Game
from os import listdir
from os.path import isfile, join

# (Pokemon Mania)

description = '''Really just a DiscordBot made for the PokemonMania server.'''

# this specifies what extensions to load when the client starts up (from this directory)
cogs_dir = "cogs"


client = commands.Bot(command_prefix='b.', description=description)
client.remove_command("help")

owner_ids = ["332177981214818315", "455322915471097857", "517729298355060736"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=Game(name='Pokemon Mania', type=1))

@client.command(pass_context=True)
async def load(ctx, extension_name : str):
    """Loads an extension."""

    if ctx.message.author.id in owner_ids:
        try:
            client.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await client.say("✅ | **{} has been successfully loaded.**".format(extension_name))
    else:
        await client.say("❌ | "+ctx.message.author.mention+", You do not have proper authorisation to use this command.")



@client.command(pass_context=True)
async def help(ctx):
    await client.say("Ask my owners to get me a good help command. Till then, help yourself.")

@client.command(pass_context=True)
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    if ctx.message.author.id in owner_ids:
        try:
            client.unload_extension(extension_name)
            await client.say("✅ | **{} has been successfully unloaded.**".format(extension_name))
        except Exception as e:
            return
    else:
        await client.say("❌ | "+ctx.message.author.mention+", You do not have proper authorisation to use this command.")


if __name__ == "__main__":
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            client.load_extension(cogs_dir + "." + extension)
        except Exception as e:
            print('Failed to load extension.')

    client.run('NTUzOTIwMDU5MTQ4NDY4MjM2.D2VFyA.OhtKCHfgGlyQgGW6eEcKIKLkZCQ')