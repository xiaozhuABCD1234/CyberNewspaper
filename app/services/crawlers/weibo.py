import requests
from utils.base_hot_list import BaseHotList


class WeiboHotList(BaseHotList):
    def __init__(self):
        super().__init__(url="https://weibo.com/ajax/side/hotSearch")

    def _parse_data(self, data) -> list[dict[str, any]]:
        hotlist = data.get("data", {}).get("realtime", [])
        result = []
        for item in hotlist:
            search_url = f"https://s.weibo.com/weibo?q={item.get('word', '')}"
            result.append(
                {
                    "title": item.get("word", ""),
                    "heat": item.get("num", ""),
                    "url": search_url,
                }
            )
        return result
