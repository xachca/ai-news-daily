def summarize_articles(articles):
    # 简化示例摘要：返回 title 作为 summary
    for article in articles:
        article["summary"] = "摘要：" + article["title"]
    return articles