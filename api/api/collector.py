from api.providers.vreddit import VReddit
from api.providers.redgifs import RedGifs
from api.providers.gfycat import GfyCat
import requests

GfyCat = GfyCat()
RedGifs = RedGifs()
VReddit = VReddit()


class Collector:
    def __init__(self) -> None:
        pass

    def writeFile(self, url, folder):
        file_blob = requests.get(url).content
        with open("./medias/" + folder + "/" + url.rsplit('/', 1)[-1], "wb") as file:
            file.write(file_blob)
            return True

    def collect(self, post, subreddit):
        try:
            if post['post_hint'] == "image":
                return self.writeFile(post['url'], subreddit)                
            if post['post_hint'] == 'link':
                pass
            if post['post_hint'] == 'rich:video':
                if post['domain'] == 'gfycat.com':
                    url = GfyCat.getDownloadUrl(post['url'])
                    return self.writeFile(url, subreddit)
                if post['domain'] == 'redgifs.com':
                    url = RedGifs.getDownloadUrl(post['url'])
                    return self.writeFile(url, subreddit)
                if post['domain'] == 'v.redd.it':
                    url = VReddit.getDownloadUrl(post['url'])
                    return self.writeFile(url, subreddit)
            return False
        except (OSError, KeyError) as e:
            return False
