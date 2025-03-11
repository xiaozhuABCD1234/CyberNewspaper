from utils.base_hot_list import BaseHotList


class CodeLifeHotList(BaseHotList):
    def _parse_data(self, data) -> list[dict[str, any]]:
        hotlist = data.get("data", {})
        result = []
        for item in hotlist:
            result.append(
                {
                    "title": item.get("title"),
                    "heat": item.get("hotValue"),
                    "url": item.get("link"),
                }
            )
        return result
