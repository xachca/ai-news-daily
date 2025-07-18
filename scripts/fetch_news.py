import feedparser
import json
from datetime import datetime

def clean_entry(entry):
    return {
        "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        "title": entry.get("title", "").strip(),
        "summary": entry.get("summary", "").strip()[:50] + "…" if len(entry.get("summary", "")) > 50 else entry.get("summary", ""),
        "url": entry.get("link", "#")
    }

def fetch_rss_entries(url, limit=10):
    try:
        feed = feedparser.parse(url)
        return [clean_entry(entry) for entry in feed.entries[:limit]]
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return []

# 真实 RSS 来源
intl_sources = [
    "https://www.reutersagency.com/feed/?best-topics=technology&post_type=best",
    "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "https://www.theverge.com/rss/index.xml"
]
china_sources = [
    "https://www.sina.com.cn/rss/tech.xml",
    "https://www.ithome.com/rss/index.xml",
    "https://www.cnbeta.com/backend.php"
]

def aggregate_news(sources, limit_per_feed=5):
    news = []
    for src in sources:
        news += fetch_rss_entries(src, limit=limit_per_feed)
    return news[:10]

# 抓取新闻
news_data = {
    "intl": aggregate_news(intl_sources),
    "china": aggregate_news(china_sources)
}

# 保存 JSON
with open("public/data/news.json", "w", encoding="utf-8") as f:
    json.dump(news_data, f, ensure_ascii=False, indent=2)

print("✅ 新闻抓取并写入完成！")