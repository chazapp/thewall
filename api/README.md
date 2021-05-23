# The Wall API
This project contains "The Wall" API.  
It is intended to provide clients with contents scrapped from Internet


## Usage

```bash
$ python3 app.py
```
This will start the API locally for your host.

## Available routes

| Route                                    | Method | Description                                                              |
|------------------------------------------|--------|--------------------------------------------------------------------------|
| /collect/<string:subreddit>              | POST   | Downloads the 100 first posts of given subreddit                         |
| /feed/<string:subreddit>                 | GET    | Returns a list of previously downloaded medias files for given subreddit |
| /medias/<string:subreddit>/<string:file> | GET    | Returns the media file                                                   |
