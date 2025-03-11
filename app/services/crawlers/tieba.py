import json
import requests
import aiohttp
from urllib.parse import unquote


def get_tieba_hotslist() -> list[dict]:
    """获取百度贴吧热门话题列表"""
    url = "https://tieba.baidu.com/hottopic/browse/topicList?res_type=0"
    result = []
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "X-Requested-With": "fetch",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查HTTP错误

        data = response.json()
        if data.get("errno") != 0:
            return []

        hot_topics = data.get("data", {}).get("bang_topic", {}).get("topic_list", [])

        for topic in hot_topics:
            result.append(
                {
                    "title": topic.get("topic_name", ""),
                    "url": unquote(topic.get("topic_url", "")),
                    "heat": str(topic.get("discuss_num", 0)),
                    "description": topic.get("topic_desc", ""),
                    "image": topic.get("topic_pic", None),
                }
            )

    except Exception as e:
        print(f"Error fetching data: {str(e)}")

    return result


# 使用示例
if __name__ == "__main__":
    topics = get_tieba_hotslist()
    for topic in topics:
        print(f"名称: {topic['topic_name']}")
        print(f"描述: {topic['topic_desc']}")
        print(f"讨论量: {topic['discuss_num']}")
        print(f"封面图片: {topic['topic_pic']}")
        print(f"链接: {topic['decoded_url']}")
        print("-" * 40)
