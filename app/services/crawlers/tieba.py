import json
import aiohttp
from urllib.parse import unquote
from utils.base_hot_list import BaseHotList


class TiebaHotList(BaseHotList):
    def __init__(self):
        super().__init__(
            url="https://tieba.baidu.com/hottopic/browse/topicList?res_type=0"
        )

    def _parse_data(self, data) -> list[dict[str, any]]:
        hot_topics = data.get("data", {}).get("bang_topic", {}).get("topic_list", [])
        result = []
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
