# scripts/fetch_summarize.py
# 示例脚本：你可以连接真实新闻API和GPT摘要服务替换这里的内容
import json
import datetime

news = [
    {
        "title": "示例标题",
        "summary": "这是一个示例摘要，用于展示自动摘要结构。",
        "link": "https://example.com"
    }
]

data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news": news
}

with open("public/data/news.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
