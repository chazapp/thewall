from flask import Blueprint, jsonify, request
import requests
from database import db
from db.post import Post, posts_schema
from .collector import Collector

API = Blueprint('api', __name__)

collector = Collector()

@API.route("/collect/<string:subreddit>", methods=["POST"])
def collect_medias_from_sub(subreddit):
    req = requests.get("https://api.reddit.com/r/" + subreddit, 
                headers={"User-Agent": "Chaz Inc. v0.0.1"},
                params={"limit": "100"}
        )
    children = req.json()['data']['children']
    collected = 0
    posts = []
    for child in children:
        try:
            post = collector.collect(child['data'], subreddit)
            if post is not None:
                posts.append(post)
                collected += 1
        except KeyError:
            pass
    db.session.add_all(posts)
    db.session.commit()
    return jsonify({"status": "ok", "collected": collected})


@API.route("/feed/<string:subreddit>", methods=['GET'])
def get_feed(subreddit):
    try:
        limit = request.args.get('limit', 25, type=int)
        offset = request.args.get('offset', 0, type=int)
        query = Post.query.filter_by(subreddit=subreddit).offset(offset).limit(limit)
        return jsonify({"feed": posts_schema.dump(query)})
    except (KeyError):
        return jsonify({"error": "bad request"}), 400
