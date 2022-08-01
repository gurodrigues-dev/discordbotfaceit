import discord
from discord.ext import commands
from requests import get

headers = {
    "accept":"application/json",
    # Insert your API Server Side Key in the line below inside the quotes
    "Authorization":f"Bearer {''}"
}

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print()
    print(f"Eu sou {bot.user} e já estou me conectando!")
    print()
    
@bot.command(name="elo")
async def send_elo(ctx, nickname: str):
    
    # URL_Details --> Obtain keyaccount, level and elo.
    
    url_players_details = f'https://open.faceit.com/data/v4/players?nickname={nickname}&game=Counter-Strike%3A%20Global%20Offensive&game_player_id={nickname}'
    response_players_details = get(url_players_details, headers=headers)
    response = (response_players_details.json())
    
    idplayer = response['player_id']
    
    # URL_Stats --> Obtain kdratio
    url_players_stats = f'https://open.faceit.com/data/v4/players/{idplayer}/stats/csgo'
    response_players_stats = get(url_players_stats, headers=headers)
    response_stats = (response_players_stats.json())
    
    # Return Dates
    
    kdratio = response_stats['lifetime']['Average K/D Ratio']
    skill_level = response['games']['csgo']['skill_level']
    eloplayer = response['games']['csgo']['faceit_elo']
    
    # Checking Level 
    
    if eloplayer > 1 and eloplayer < 800:
        points = 801 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 801 and eloplayer < 950:
        points = 951 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
    
    if eloplayer >= 951 and eloplayer < 1100:
        points = 1101 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 1101 and eloplayer < 1250:
        points = 1251 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 1251 and eloplayer < 1400:
        points = 1401 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 1401 and eloplayer < 1550:
        points = 1551 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 1551 and eloplayer < 1700:
        points = 1701 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 1701 and eloplayer < 1850:
        points = 1851 - eloplayer
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 1851 and eloplayer < 2000:
        points = 2001 - eloplayer 
        response = f'Você está no nível {skill_level}, faltam {points} pontos para subir de nível e seu k/d é {kdratio}'
        
    if eloplayer >= 2001:
        points = eloplayer - 2000
        response = f'Você está no nível {skill_level}, faltam {points} pontos para cair de nível e seu k/d é {kdratio}'
    
    await ctx.send(response)
    
# Insert your bot's token on discord here
bot.run('')
