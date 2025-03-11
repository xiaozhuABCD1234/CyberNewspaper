import json
import aiohttp
from urllib.parse import unquote


async def get_tieba_hotslist() -> list[dict]:
    """获取百度贴吧热门话题列表"""
    url = "https://tieba.baidu.com/hottopic/browse/topicList?res_type=0"
    result = []
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "X-Requested-With": "fetch",
    }
    async with aiohttp.ClientSession() as session:
        try:

            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return []

                data = await response.json()
                if data.get("errno") != 0:
                    return []

                hot_topics = (
                    data.get("data", {}).get("bang_topic", {}).get("topic_list", [])
                )
                for topic in hot_topics:
                    result.append(
                        {
                            "title": topic.get("topic_name", ""),
                            "url": unquote(topic.get("topic_url", "")),
                            "heat": topic.get("discuss_num", 0),
                            "description": topic.get("topic_desc", ""),
                            "image": topic.get("topic_pic", None),
                        }
                    )
                return result
        except Exception as e:
            print(f"请求失败: {e}")
            return []
