from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

async def hcim_death():
    hardcores=[]
    print("Running...")
    for x in range(0, 40):
        url = 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/overall?table=0&page=' + str(x)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        highscores = soup.find(id="contentHiscores")
        table = highscores.find('tbody')
        # alive = table.find_all(class_="personal-hiscores__row")
        dead = table.find_all(class_="personal-hiscores__row personal-hiscores__row--dead")
        f = open("dead_hardcores.json", "r")
        hcim = json.load(f)
        for i in dead:
            rsn = i.find('a')
            if rsn.string not in hcim["rsn"]:
                hcim["rsn"].append(rsn.string)
                newrsn = rsn.string.replace(" ", "%A0")
                hardcores.append(newrsn)
        with open('dead_hardcores.json', 'w') as f:
            json.dump(hcim, f, indent=4)
        f.close()
    print("Returning...")
    return hardcores
