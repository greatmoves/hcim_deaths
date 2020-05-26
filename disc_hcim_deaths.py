import asyncio
from discord.ext import commands
from hcim_deaths_bot import hcim_death
from rshighscores import gethighscores

client = commands.Bot(command_prefix='!', help_command=None, owner_id=OWNER_ID)


@client.event
async def on_ready():
    print('Ready to find dead hardcores...')


async def background_loop():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        hcims = await hcim_death()
        if len(hcims) > 0:
            for i in hcims:
                await channel.send(embed=gethighscores(i))
        await asyncio.sleep(60*20)  # checks every 20 minutes.


client.loop.create_task(background_loop())
client.run('TOKEN')
