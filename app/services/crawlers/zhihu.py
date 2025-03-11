import requests
import json


def fetch_zhihu_hotlist() -> list[dict]:
    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "X-Requested-With": "fetch",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查HTTP状态码
        data = response.json()
        hotlist = data.get("data", [])

        # 提取核心数据
        result = []
        for item in hotlist:
            target = item.get("target", {})
            children = item.get("children", [])
            thumbnail = (
                children[0].get("thumbnail", "") if children else ""
            )  # 提取封面图片

            result.append(
                {
                    "title": target.get("title"),
                    "heat": item.get("detail_text"),
                    "url": f"https://www.zhihu.com/question/{target.get('id')}",  # 拼接实际访问URL
                    "answer_count": target.get("answer_count"),
                    "thumbnail": thumbnail,  # 添加封面图片
                }
            )
        return result
    except Exception as e:
        print(f"请求失败: {e}")
        return []


# 调用示例
hotlist = fetch_zhihu_hotlist()
for idx, item in enumerate(hotlist, 1):
    print(f"{idx}. {item['title']} | 热度：{item['heat']}")
    print(f"链接: {item['url']}")
    print(f"封面图片: {item['thumbnail']}")
    print("-" * 40)
