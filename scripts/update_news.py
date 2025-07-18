
import json
from scripts.fetch_news import fetch_news
from scripts.fetch_summarize import summarize

def main():
    news_items = fetch_news()
    summarized_news = []

    for item in news_items:
        title = item.get("title")
        content = item.get("content")
        url = item.get("url")

        summary = summarize(content)

        summarized_news.append({
            "title": title,
            "summary": summary,
            "url": url
        })

    with open("public/data/news.json", "w", encoding="utf-8") as f:
        json.dump(summarized_news, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
