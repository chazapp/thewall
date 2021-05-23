from api.collector import Collector
from flask import Blueprint, jsonify, send_file
import requests
import mimetypes
import os
from .collector import Collector


API = Blueprint('api', __name__)

collector = Collector()

@API.route("/collect/<string:subreddit>", methods=["POST"])
def collect_medias_from_sub(subreddit):
    try:
        os.mkdir("./medias/" + subreddit)
    except OSError as e:
        pass
    req = requests.get("https://api.reddit.com/r/" + subreddit, 
                headers={"User-Agent": "Chaz Inc. v0.0.1"},
                params={"limit": "100"}
        )
    children = req.json()['data']['children']
    downloaded = 0
    for child in children:
        try:
            if collector.collect(child['data'], subreddit):
                downloaded += 1
        except KeyError:
            pass
    return jsonify({"status": "ok", "downloaded": downloaded})


@API.route("/feed/<string:subreddit>", methods=['GET'])
def get_feed(subreddit):
    try:
        files = os.listdir('./medias/'+subreddit)
        resp = []
        for file in files:
            resp.append('http://localhost:8080/medias/' + subreddit + '/' + file)
        return jsonify({"feed": resp})
    except OSError:
        return jsonify({"error": "no feed available"}), 404

@API.route("/medias/<string:subreddit>/<string:file>", methods=['GET'])
def get_media(subreddit, file):
    try:
        path = 'medias/' + subreddit + '/' + file
        mimetype = mimetypes.guess_type(path)[0]
        print("Sending file: ", path, " with mimetype:", mimetype)
        return send_file(path, mimetype=mimetype)
    except OSError as e:
        print(e)
        pass