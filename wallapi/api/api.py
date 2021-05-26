from flask import Blueprint, jsonify, request
import requests
import json
from database import db
from sqlalchemy.sql.expression import func
from db.post import Post, posts_schema
from .collector import Collector

API = Blueprint('api', __name__)

collector = Collector()

@API.route("/collect/<string:subreddit>", methods=["POST"])
def collect_medias_from_sub(subreddit):
    req = requests.get("https://api.reddit.com/r/" + subreddit + "/top?t=day", 
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
                exists = Post.query.filter_by(content=post.content).first() is not None
                if not exists:
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

@API.route("/feed", methods=['GET'])
def get_random_feed():
    try:
        nsfw = request.args.get('nsfw', False, type=json.loads)
        limit = request.args.get('limit', 25, type=int)
        offset = request.args.get('offset', 0, type=int)
        query = Post.query.filter_by(nsfw=nsfw).order_by(func.random()).offset(offset).limit(limit)
        return jsonify({"feed": posts_schema.dump(query)}), 200
    except KeyError:
        return jsonify({"error": "bad request"}), 400