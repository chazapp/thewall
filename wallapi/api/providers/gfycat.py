import requests
from requests import api
from requests.api import request

class GfyCat:
    def __init__(self):
        pass
    
    def getDownloadUrl(self, gfycatURL):
        apiURL = "https://api.gfycat.com/v1/gfycats/" + gfycatURL.rsplit('/', 1)[-1]
        gfyItem = requests.get(apiURL).json()
        return gfyItem['gfyItem']['content_urls']['mp4']['url']