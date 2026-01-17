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

def fetch_dd_posts(count:int = 100):
    subreddit = reddit.subreddit("wallstreetbets")
    posts = []

    for post in subreddit.new(limit=count):
        if post.link_flair_text == "DD":
            post_data = {
                'id': post.id,
                'author': post.author,
                'created_time (utc)': post.created_utc,
                'post_title': post.title,
                'text': post.selftext,
                'upvote_count': post.score,
                'upvote_ratio': post.upvote_ratio
            }

            posts.append(post_data)
    
    return posts

def main():
    posts = fetch_dd_posts()

if __name__ == "__main__":
    main()