# setup imports
import discord
from discord.ext import commands
import psutil


processes = {
    "ark": "ArkAscendedServer.exe",
    "palworld": "PalServer-Win64-Shipping-Cmd.exe",
    "enshrouded": "enshrouded.exe",
    }


class Hosting(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def server(self, ctx):

        running_processes = []

        for name, process_name in processes.items():
            if any(proc.name() == process_name for proc in psutil.process_iter()):
                running_processes.append(f"**{name}**")

        if running_processes:
            await ctx.send(f"The following server(s) are running:   {', '.join(running_processes)}.")
        else:
            await ctx.send("No specified servers are currently running.")


async def setup(client):
    await client.add_cog(Hosting(client))

