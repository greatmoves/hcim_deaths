from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import discord

def gethighscores(rsn):
    newrsn = rsn.replace(" ", "%A0")
    url = 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/hiscorepersonal?user1='+str(newrsn)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    highscores = soup.find(id="contentHiscores")
    try:
        skills = highscores.find('table')
    except AttributeError:
        return -1
    table = skills.find_all('td')
    for i in range(len(table) -1,-1,-1):
        if table[i].string == None:
            del table[i]
        table[i].string = table[i].string.replace("\n", "")
    del table[:5]
    embed = discord.Embed(title=str(rsn.replace("%A0", " ")) + " has died!", url=str(url), colour=0xFF00CC)
    overall_info = "Rank = " + str(table[1].string) + ", Level = " + str(table[2].string) + ", Xp = " + str(table[3].string)
    embed.add_field(name=table[0].string, value=overall_info, inline=True)
    x = 4
    while x < 24*4:
        info = "Rank = " + str(table[x+1].string) + ", Level = " + str(table[x+2].string) + ", Xp = " + str(
            table[x+3].string)
        embed.add_field(name=table[x].string, value=info, inline=True)
        x+=4
    #j = x This would add minigames, but the maximum amount of fields in an embed is 25
    #while j < len(table):
    #    info = "Rank = " + str(table[j+1].string) + " Score = " + str(table[j+2].string)
    #    embed.add_field(name=table[j].string, value=info, inline=True)
    #    j+=3

    return embed