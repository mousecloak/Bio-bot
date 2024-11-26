# setup imports
import discord
from discord.ext import commands

# set common variables
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


role_map = {
    "Juicers": 12345,
    "COD": 12345,
    "PGA": 12345,
    "Palworld": 12345
}

color_roles = {
    "red": 12345,
    "orange": 12345,
    "yellow": 12345,
    "green": 12345,
    "blue": 12345,
    "purple": 12345,
    "pink": 12345,
    "grey": 12345,
    "black": 12345,
    "white": 12345
}


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @client.command()
    async def group(self, ctx, keyword: str):        
        role_id = role_map.get(keyword)
        
        if role_id:
            role = discord.utils.get(ctx.guild.roles, id=role_id)
            
            if role:
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


    @client.command()
    async def color(self, ctx, color: str):
        role_id = color_roles.get(color.lower())

        if role_id:
            role = discord.utils.get(ctx.guild.roles, id=role_id)
            
            if role:
                if role in ctx.author.roles:
                    await ctx.send(f'{ctx.author.mention}, you already have the {role.name} role.')
                    return

                # Remove existing color roles
                existing_roles = [discord.utils.get(ctx.guild.roles, id=id) for id in color_roles.values()]
                for existing_role in existing_roles:
                    if existing_role in ctx.author.roles:
                        await ctx.author.remove_roles(existing_role)

                # Add the new role
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention} has been added to the {role.name}!')

            else:
                await ctx.send(f'Role with ID "{role_id}" not found.')
        else:
            await ctx.send(f'Color "{color}" not recognized.')


async def setup(client):
    await client.add_cog(Admin(client))
    
