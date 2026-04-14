import requests
from dotenv import load_dotenv
import os
import json
import asyncio


load_dotenv()



async def GetImage():
    x = requests.get("https://api.mozambiquehe.re/assets/ranks/platinum2.png")
    if x.status_code == 200:
        with open("plat.png","wb") as f:
            f.write(x.content)

async def GetPlayerData():
    key = os.getenv('APIKEY')
    player = 'Fui96'
    Platform = 'PC'

    x = requests.get(f'https://api.mozambiquehe.re/bridge?auth={key}&player={player}&platform={Platform}')
    
    if x.status_code == 200:
        y = json.loads(x.text)
        
        with open("data.json",'w') as f:
            json.dump(y,f,indent=4)


        
# asyncio.run(GetImage())
asyncio.run(GetPlayerData())