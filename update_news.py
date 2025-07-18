import os
import json
from fetch_news import fetch_news
from fetch_summarize import summarize_articles

OUTPUT_PATH = 'public/data/news.json'

def update_news():
    print("Fetching news articles...")
    articles = fetch_news()
    print(f"Fetched {len(articles)} articles.")

    print("Summarizing articles...")
    for article in articles:
        summary = summarize_articles(article['content'])
        article['summary'] = summary

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    print(f"Saving summarized news to {OUTPUT_PATH}...")
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print("News update complete.")

if __name__ == '__main__':
    update_news()
