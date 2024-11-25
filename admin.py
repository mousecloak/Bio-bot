# setup imports
import discord
from discord.ext import commands
from discord import Embed, Member
import asyncio


# set common variables
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @client.command()
    async def group(self, ctx, keyword: str):
        # Define a mapping of keywords to role IDs
        role_map = {
            "Juicers": 12345,
            "COD": 12345,
            "PGA": 12345,
            "Palworld": 12345
        }
        
        # Check if the keyword exists in the mapping
        role_id = role_map.get(keyword)
        
        if role_id:
            # Find the role in the guild using the role ID
            role = discord.utils.get(ctx.guild.roles, id=role_id)
            
            if role:
                # Toggle the role
                if role in ctx.author.roles:
                    await ctx.author.remove_roles(role)
                    await ctx.send(f'Removed role: {role.name}')
                else:
                    await ctx.author.add_roles(role)
                    await ctx.send(f'Added role: {role.name}')
            else:
                await ctx.send(f'Role with ID "{role_id}" not found.')
        else:
            await ctx.send('Invalid keyword. Please use a valid keyword.')



async def setup(client):
    await client.add_cog(Admin(client))
    
