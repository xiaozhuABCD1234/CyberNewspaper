import aiohttp
import json


class BaseHotList:
    BASE_HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "X-Requested-With": "fetch",
    }

    def __init__(self, url: str):
        self.url = url
        self.session = aiohttp.ClientSession(headers=self.BASE_HEADERS)

    async def _fetch_data(self, url=None) -> dict:
        if url is None:
            url = self.url  # 默认使用实例的 url 属性
        try:
            async with self.session.get(url) as response:
                response.raise_for_status()
                return await response.json()
        except Exception as e:
            print(f"请求失败: {e}")
            return None

    async def get_hot_list(self) -> list[dict[str, any]]:
        data = await self._fetch_data()
        if data is None:
            return []
        return self._parse_data(data)

    def _parse_data(self, data: dict[str, any]) -> list[dict[str, any]]:
        # 子类需重写此方法
        raise NotImplementedError("必须实现数据解析方法")

    async def close(self):
        await self.session.close()
