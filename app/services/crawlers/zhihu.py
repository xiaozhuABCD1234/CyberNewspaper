from utils.base_hot_list import BaseHotList
from urllib.parse import unquote
from utils.utils import convert_to_number


class ZhihuHotList(BaseHotList):
    def __init__(self):
        super().__init__(
            url="https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50"
        )

    def _parse_data(self, data) -> list[dict[str, any]]:
        hotlist = data.get("data", [])
        result = []
        for item in hotlist:
            target = item.get("target", {})
            children = item.get("children", [])
            thumbnail = children[0].get("thumbnail") if children else None

            result.append(
                {
                    "title": target.get("title"),
                    "heat": convert_to_number(item.get("detail_text")),
                    "url": f"https://www.zhihu.com/question/{target.get('id')}",
                    "image": thumbnail,
                    "description": target.get("excerpt"),
                }
            )
        return result
