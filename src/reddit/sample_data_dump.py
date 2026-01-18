from src.reddit import fetch_dd_posts
import json
from pathlib import Path

dd_posts = fetch_dd_posts(500)

filtered_dd_posts = [
    {
        "post_title": post.get("post_title"),
        "text": post.get("text")
    }
    for post in dd_posts
]

output_path = Path("src/reddit/data/sample.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as f:
    json.dump(filtered_dd_posts, f, indent=4, ensure_ascii=False)