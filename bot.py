import discord
import requests
import json
import urllib
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

bot.remove_command('help')

@bot.command()
async def eu(pname):
    r = requests.get('http://api.wf.my.com/user/stat/?name=' + pname + '&server=1')
    x = json.loads(r.text)
    pvp = "K/D = " + str(x['pvp']) + "\n" + "Kill = " + str(x['kills']) + "\n" + "Death = " + str(x['death']) + "\n" + "Favourite class = " + str(x['favoritPVP']) + "\n" + "Wins = " + str(x['pvp_wins']) + "\n" + "Lost = " + str(x['pvp_lost'])
    pve = "K/D = " + str(x['pve']) + "\n" + "Kill = " + str(x['pve_kills']) + "\n" + "Death = " + str(x['pve_death']) + "\n" + "Favourite class = " + str(x['favoritPVE']) + "\n" + "Wins = " + str(x['pve_wins']) + "\n" + "Lost = " + str(x['pve_lost'])
    stat = "Nickname = " + str(x['nickname']) + "\n Rank = " + str(x['rank_id']) + "\n Experience points = " + str(x['experience']) + "\n Play time = " + str(x['playtime_h']) + "H"
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Player statistics", value=stat, inline=False)
    embed.add_field(name="PVP", value=pvp, inline=False)
    embed.add_field(name="PVE", value=pve, inline=False)
    await bot.say(embed=embed)

@bot.command()
async def na(pname):
    r = requests.get('http://api.wf.my.com/user/stat/?name=' + pname + '&server=2')
    x = json.loads(r.text)
    pvp = "K/D = " + str(x['pvp']) + "\n" + "Kill = " + str(x['kills']) + "\n" + "Death = " + str(x['death']) + "\n" + "Favourite class = " + str(x['favoritPVP']) + "\n" + "Wins = " + str(x['pvp_wins']) + "\n" + "Lost = " + str(x['pvp_lost'])
    pve = "K/D = " + str(x['pve']) + "\n" + "Kill = " + str(x['pve_kills']) + "\n" + "Death = " + str(x['pve_death']) + "\n" + "Favourite class = " + str(x['favoritPVE']) + "\n" + "Wins = " + str(x['pve_wins']) + "\n" + "Lost = " + str(x['pve_lost'])
    stat = "Nickname = " + str(x['nickname']) + "\n Rank = " + str(x['rank_id']) + "\n Experience points = " + str(x['experience']) + "\n Play time = " + str(x['playtime_h']) + "H"
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Player statistics", value=stat, inline=False)
    embed.add_field(name="PVP", value=pvp, inline=False)
    embed.add_field(name="PVE", value=pve, inline=False)
    await bot.say(embed=embed)

bot.run('NDc3ODAwOTMwODQzMDMzNjAw.DlBadw.AXAnSbsT4ekEmGQ6VcgclQuIwlU')
