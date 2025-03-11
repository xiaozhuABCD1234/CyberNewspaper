from utils.base_hot_list import BaseHotList


class BaiduHotList(BaseHotList):
    def __init__(self):
        super().__init__(url="https://top.baidu.com/api/board?tab=realtime")

    def _parse_data(self, data: dict[str, any]) -> list[dict[str, any]]:
        cards = data.get("data", {}).get("cards", [])
        hotlist = []
        for card in cards:
            content = card.get("content", [])
            hotlist.extend(content)
        result = []
        for item in hotlist:
            result.append(
                {
                    "title": item.get("query", ""),
                    "heat": item.get("hotScore", ""),
                    "url": item.get("rawUrl", ""),
                    "description": item.get("desc", ""),
                    "image": item.get("img", ""),
                }
            )
        return result
