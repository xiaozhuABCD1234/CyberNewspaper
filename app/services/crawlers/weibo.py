import requests


def get_weibo_hotlist() -> list[dict]:
    url = "https://weibo.com/ajax/side/hotSearch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查HTTP请求是否成功

        data = response.json()
        hotlist = data.get("data", {}).get("realtime", [])

        if not hotlist:
            print("未找到实时热搜数据，请检查返回的JSON结构。")
            return []

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
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP错误: {http_err}")
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        return []
    except requests.exceptions.RequestException as req_err:
        print(f"请求错误: {req_err}")
        return []
    except Exception as e:
        print(f"其他错误: {e}")
        return []


if __name__ == "__main__":
    # 调用函数获取微博热搜列表
    weibo_hotlist = get_weibo_hotlist()

    # 检查是否获取到数据
    if not weibo_hotlist:
        print("未能获取到微博热搜数据，请检查网络或API是否正常。")

    # 打印热搜列表
    print("微博热搜列表：")
    for index, item in enumerate(weibo_hotlist, start=1):
        print(f"{index}. {item['title']} (热度: {item['heat']})")
        print(f"   搜索链接: {item['url']}")
        print("-" * 40)  # 分隔线，方便查看
