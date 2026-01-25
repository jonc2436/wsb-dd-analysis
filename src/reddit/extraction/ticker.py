import re
import json
from collections import defaultdict

TICKER_RE = re.compile(r"\$([A-Z]{1,5})\b")

def extract_tickers(text : str) -> list[str]:
    return TICKER_RE.findall(text)

with open("src/reddit/data/sample.json", encoding="utf-8") as f:
    posts = json.load(f)

final_data = {}

for post in posts:
    post_id = post['post_id']
    tickers = defaultdict(lambda: {'title': 0, 'body': 0})

    for t in extract_tickers(post.get('post_title', "")):
        tickers[t]['title'] += 1
    
    for t in extract_tickers(post.get('text', "")):
        tickers[t]['body'] += 1
    
    scores = {
        t: counts['title'] * 5 + counts['body'] * 1 for t, counts in tickers.items()
    }

    final_data[post_id] = {
        'counts': dict(tickers),
        'scores': scores,
        'top': max(scores, key=scores.get) if scores else None
    }