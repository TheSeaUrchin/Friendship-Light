#File for discord interactions
import WIFI
import network
import urequests
import ujson
WIFI.connect()
token = '[you bot token here]'
URL_GET_G = 'https://discord.com/api/v10/channels/{your channel ID}/messages?limit=1'
URL_POST_G = 'https://discord.com/api/v10/channels/{your channel ID}/messages'
ID = '5'
ID2 = '5'
URL_GET_S = 'https://discord.com/api/v10/channels/{your channel ID}/messages?limit=1'
URL_POST_S = 'https://discord.com/api/v10/channels/{your channel ID}/messages'

def send(URL, content):
    post_data = ujson.dumps({ 'content': content, 'embeds' : []})
    urequests.post(url = URL, headers={'Authorization': token,'content-type': 'application/json'}, data = post_data)

def getData(URL):
    global ID
    res = urequests.get(url=URL,headers={'Authorization': token})
    JSON = res.json()[0]
    if JSON['id'] != ID:
        ID = JSON['id']
        return JSON['content']
    else:
        return "none"
        
def start():
    global ID2
    res = urequests.get(url=URL_GET_S,headers={'Authorization': token})
    JSON = res.json()[0]
    ID2 = JSON['id']

def getDataS():
    global ID2
    res = urequests.get(url=URL_GET_S,headers={'Authorization': token})
    JSON = res.json()[0]
    if JSON['id'] != ID2:
        ID2 = JSON['id']
        return JSON['content']
    else:
        return "none"
 


