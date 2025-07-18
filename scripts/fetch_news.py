import requests
from datetime import datetime

def fetch_news():
    # 示例数据结构（模拟）
    return [
        {
            "title": "OpenAI 发布全新 GPT 模型",
            "url": "https://example.com/openai-gpt-news",
            "source": "OpenAI Blog",
            "published": datetime.utcnow().isoformat()
        },
        {
            "title": "Google DeepMind 最新 AI 成果发布",
            "url": "https://example.com/deepmind-ai-news",
            "source": "Google Research",
            "published": datetime.utcnow().isoformat()
        }
    ]