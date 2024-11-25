# setup imports
import discord
from discord.ext import commands
import psutil

class Hosting(commands.Cog):
    def __init__(self, client):
        self.client = client





# Create an array of .exe and have the bot comb to see if any are running, if so, reply with game thats currently running.

# create list of login details (IP, port, password) to login



    @commands.command()
    async def server(self, ctx, *, arg):
        if arg.lower() == "ark":
            process_name = "ArkAscendedServer.exe"
            # Check if the process is running
            if any(proc.name() == process_name for proc in psutil.process_iter()):
                await ctx.send(f"Ark server is running.")
            else:
                await ctx.send(f"Ark server is not running.")
        else:
            await ctx.send("Status unknown, please contact host.")


async def setup(client):
    await client.add_cog(Hosting(client))

