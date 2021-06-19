from SheebaQueen.events import register
from telethon import Button
from PIL import Image, ImageDraw, ImageFont


@register(pattern="^/game")

async def game(event): 

    await event.reply(
TOKEN = ".........."
url = "https://api.telegram.org/bot" + TOKEN
requests.get(url + '/sendGame?chat_id=' + id + '&game_short_name=' + text)

)


@register(pattern="^/no")

async def no(event): 

      await event.reply(
buttons=[[Button.url("2048 game ",url="sheebaga.heliohost.us")]])
#pokemon sluce

@register(pattern="^/slice")

async def slice(event): 

      await event.reply("Some Games By Me"
,buttons=[[Button.url("Pokeball slice ",url="sheebaga.heliohost.us/pokemonslice.html")]])

#Rom run

@register(pattern="^/run")

async def run(event): 

      await event.reply("Some Games By Me"
,buttons=[[Button.url("Rom Run ",url="https://games.cdn.famobi.com/html5games/o/om-nom-run/v1140/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=abe80572-560a-444d-baf7-2fa4a7b2c02f&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=177&original_ref=android-app%3A%2F%2Forg.telegram.messenger%2F")]])

#treasure hunt
@register(pattern="^/hunt")
async def hunt(event):
      
       await event.reply("Treasure Hunt Game",
buttons=[[Button.url("Treasure Hunt",url="https://www.hiddenobjectgames.com/game/Jungle+Mysteries")]])

#ludo 
@register(pattern="^/ludo")

async def hunt(event):

      

       await event.reply("Ludo Game",

buttons=[[Button.url("Play Ludo Game",url="https://poki.com/en/g/ludo-multiplayer#fullscreen")]])



__mod_name__ = "Game"
__help__ ="""
 /hunt ==>> Treasure Hunt Game games
/run ===>> Running Game
/no ==>> 2048 block No. making game
/slice ===>> Slice The pokeball (like fruit slice in mpl)
/ludo ==>> play ludo 



"""




