import os
from dotenv import load_dotenv
import praw

load_dotenv()

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = os.getenv("USER_AGENT")

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    username = REDDIT_USERNAME,
    password = REDDIT_PASSWORD,
    user_agent = USER_AGENT
)

subreddit = reddit.subreddit("wallstreetbets")

dd_posts = []

for post in subreddit.new(limit=1000):
    if post.link_flair_text == "DD":
        dd_posts.append({
            "id": post.id,
            "title": post.title,
            "score": post.score,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc
        })