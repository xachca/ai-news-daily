import os
import json
from fetch_news import fetch_news
from fetch_summarize import summarize_articles

def main():
    articles = fetch_news()
    summarized_articles = summarize_articles(articles)

    # 确保 public/data 目录存在
    output_dir = os.path.join("public", "data")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "news.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summarized_articles, f, ensure_ascii=False, indent=2)

    print("✅ 新闻抓取并写入完成！")

if __name__ == "__main__":
    main()