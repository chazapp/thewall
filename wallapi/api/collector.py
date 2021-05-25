from .providers.vreddit import VReddit
from .providers.redgifs import RedGifs
from .providers.gfycat import GfyCat
import requests
from db.post import Post
from database import db
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

    def collect(self, item, subreddit):
        try:
            url = ''
            type = ''
            if item['post_hint'] == "image":
                url = item['url']
                type = 'image'
            elif item['post_hint'] == 'link':
                if item['url'].rsplit('.', 1)[-1] == 'gifv':
                    url = item['url']
                    type = 'video'
                else:
                    raise KeyError
            elif item['post_hint'] == 'rich:video':
                if item['domain'] == 'gfycat.com':
                    url = GfyCat.getDownloadUrl(item['url'])
                    type = 'video'
                elif item['domain'] == 'redgifs.com':
                    url = RedGifs.getDownloadUrl(item['url'])
                    type = 'video'
                elif item['domain'] == 'v.redd.it':
                    raise KeyError
                    # url = VReddit.getDownloadUrl(item['url'])
                    # type = 'video'
                else:
                    raise KeyError
            else:
                raise KeyError
            post = Post(
                content=url,
                title=item['title'],
                post_url="https://reddit.com" + item['permalink'],
                subreddit=subreddit,
                type=type,
                nsfw=item['over_18']
            )
            return post
        except (OSError, KeyError) as e:
            return None
