from database import db, ma

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    title = db.Column(db.String())
    post_url = db.Column(db.String())
    subreddit = db.Column(db.String())
    type = db.Column(db.String())
    nsfw = db.Column(db.Boolean())

    def __init__(self, content, title, post_url, subreddit, type, nsfw):
        self.content = content
        self.title = title
        self.post_url = post_url
        self.subreddit = subreddit
        self.type = type
        self.nsfw = nsfw

    def __repr__(self):
        return '<Post %r>' % self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ("content", "title", "post_url", "subreddit", "type", "nsfw")

post_schema = PostSchema()
posts_schema = PostSchema(many=True)