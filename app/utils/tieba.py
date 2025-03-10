import json
import requests
from urllib.parse import unquote

def get_tieba_hots() -> list[dict]:
    """获取百度贴吧热门话题列表"""
    url = "https://tieba.baidu.com/hottopic/browse/topicList?res_type=0"
    result = []
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 检查HTTP错误
        
        data = response.json()
        if data.get("errno") != 0:
            return []
            
        hot_topics = data.get("data", {}).get("bang_topic", {}).get("topic_list", [])
        
        for topic in hot_topics:
            result.append({
                "topic_name": topic.get("topic_name", ""),
                "topic_desc": topic.get("topic_desc", ""),
                "discuss_num": topic.get("discuss_num", 0),
                # "original_url": topic.get("topic_url", ""),
                "decoded_url": unquote(topic.get("topic_url", ""))
            })
            
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
    
    return result

# 使用示例
if __name__ == "__main__":
    topics = get_tieba_hots()
    for topic in topics:
        print(f"名称: {topic['topic_name']}")
        print(f"描述: {topic['topic_desc']}")
        print(f"讨论量: {topic['discuss_num']}")
        print(f"链接: {topic['decoded_url']}")
        print("-" * 40)