import requests
import json


def get_bilibili_ranking() -> list[dict] | None:
    url = "https://api.bilibili.com/x/web-interface/ranking/v2?type=all"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("code") != 0:
            print(f"API返回错误: {data.get('message', '未知错误')}")
            return None

        video_list = data.get("data", {}).get("list", [])
        result = []

        for video in video_list:
            video_info = {
                "title": video.get("title", "无标题"),
                "view": video.get("stat", {}).get("view", 0),
                "danmaku": video.get("stat", {}).get("danmaku", 0),
                "like": video.get("stat", {}).get("like", 0),
                "up": video.get("owner", {}).get("name", "未知UP主"),
                "bvid": video.get("bvid", ""),
                "url": f"https://www.bilibili.com/video/{video.get('bvid', '')}",
                "cover": video.get("pic", ""),  # 添加封面链接
            }
            result.append(video_info)

        return result

    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {str(e)}")
    except json.JSONDecodeError:
        print("响应数据解析失败")
    except Exception as e:
        print(f"未知错误: {str(e)}")

    return None


def get_bilibili_popular() -> list[dict]:
    url = "https://api.bilibili.com/x/web-interface/popular"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("code") != 0:
            print(f"API返回错误: {data.get('message', '未知错误')}")
            return None

        video_list = data.get("data", {}).get("list", [])
        result = []

        for video in video_list:
            video_info = {
                "title": video.get("title", "无标题"),
                "view": video.get("stat", {}).get("view", 0),
                "danmaku": video.get("stat", {}).get("danmaku", 0),
                "like": video.get("stat", {}).get("like", 0),
                "up": video.get("owner", {}).get("name", "未知UP主"),
                "bvid": video.get("bvid", ""),
                "url": f"https://www.bilibili.com/video/{video.get('bvid', '')}",
                "cover": video.get("pic", ""),  # 添加封面链接
            }
            result.append(video_info)

        return result

    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {str(e)}")
    except json.JSONDecodeError:
        print("响应数据解析失败")
    except Exception as e:
        print(f"未知错误: {str(e)}")

    return None


# 使用示例
if __name__ == "__main__":
    ranking_data = get_bilibili_popular()

    if ranking_data:
        print(f"成功获取 {len(ranking_data)} 条热门视频")
        for index, video in enumerate(ranking_data[:3], 1):  # 展示前3条
            print(f"{index}. [{video['up']}] {video['title']}")
            print(
                f"   播放：{video['view']} | 弹幕：{video['danmaku']} | 点赞：{video['like']}"
            )
            print(f"   封面：{video['cover']}")
            print(f"   链接：{video['url']}")
            print("-" * 80)
    else:
        print("未能获取排行榜数据")
