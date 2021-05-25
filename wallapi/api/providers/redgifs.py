import requests
from requests import api
from requests.api import request


class RedGifs:
    def __init__(self):
        pass
    
    def getDownloadUrl(self, redGifURL):
        apiURL = "https://api.redgifs.com/v1/gfycats/" + redGifURL.rsplit('/', 1)[-1]
        redItem = requests.get(apiURL)
        downloadURL = redItem.json()['gfyItem']['content_urls']['mp4']['url']
        return downloadURL
