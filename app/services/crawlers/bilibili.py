import aiohttp
from typing import List, Dict, Optional


async def fetch_bilibili_data(url: str) -> Optional[dict]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=10)
        ) as session:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.json()

    except aiohttp.ClientError as e:
        print(f"网络请求失败: {str(e)}")
    except Exception as e:
        print(f"发生未知错误: {str(e)}")
    return None


def process_video_data(video: dict) -> Dict:
    return {
        "title": video.get("title", "无标题"),
        "url": f"https://www.bilibili.com/video/{video.get('bvid', '')}",
        "heat": video.get("stat", {}).get("view", 0),
        # "danmaku": video.get("stat", {}).get("danmaku", 0),
        # "like": video.get("stat", {}).get("like", 0),
        "description": video.get("desc"),
        "author": video.get("owner", {}).get("name", "未知UP主"),
        # "bvid": video.get("bvid", ""),
        "image": video.get("pic", ""),
    }


async def get_bilibili_ranking() -> Optional[List[Dict]]:
    url = "https://api.bilibili.com/x/web-interface/ranking/v2?type=all"
    data = await fetch_bilibili_data(url)

    if data and data.get("code") == 0:
        return [process_video_data(v) for v in data.get("data", {}).get("list", [])]

    print(f"排行榜数据获取失败: {data.get('message', '未知错误')}" if data else "")
    return None


async def get_bilibili_popular() -> Optional[List[Dict]]:
    url = "https://api.bilibili.com/x/web-interface/popular"
    data = await fetch_bilibili_data(url)

    if data and data.get("code") == 0:
        return [process_video_data(v) for v in data.get("data", {}).get("list", [])]

    print(f"热门数据获取失败: {data.get('message', '未知错误')}" if data else "")
    return None
