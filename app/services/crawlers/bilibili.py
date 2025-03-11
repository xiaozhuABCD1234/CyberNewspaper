from utils.base_hot_list import BaseHotList


class BilibiliHotList(BaseHotList):
    def __init__(self):
        super().__init__(
            url="https://api.bilibili.com/x/web-interface/ranking/v2?type=all"
        )

    def _parse_data(self, data: dict) -> list[dict[str, any]]:
        if data.get("code") != 0:
            return []  # API 返回错误时返回空列表
        hotlist = data.get("data", {}).get("list", [])
        result = []
        for item in hotlist:
            result.append(
                {
                    "title": item.get("title"),
                    "heat": item.get("stat", {}).get("view", 0),
                    "url": f"https://www.bilibili.com/video/{item.get('bvid', '')}",
                    "description": item.get("desc"),
                    "author": item.get("owner", {}).get("name", "未知UP主"),
                    "image": item.get("pic", ""),
                }
            )
        return result

    async def get_bilibili_ranking(self) -> list[dict[str, any]] | None:
        """获取排名数据（与 get_hot_list() 功能相同）"""
        data = await self._fetch_data()  # 使用初始化的 URL（排名接口）
        if data is None:
            return None
        return self._parse_data(data)  # 直接传入整个 data

    async def get_bilibili_popular(self) -> list[dict[str, any]] | None:
        """获取热门数据（使用不同的 URL）"""
        url = "https://api.bilibili.com/x/web-interface/popular"
        data = await self._fetch_data(url=url)  # 传入热门接口的 URL
        if data is None:
            return None
        return self._parse_data(data)  # 直接传入整个 data
