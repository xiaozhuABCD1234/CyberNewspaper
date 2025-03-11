from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def get_bing_hotlist() -> list[dict]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # 打开浏览器
        context = browser.new_context()
        page = context.new_page()

        # 打开目标网页并等待加载完成
        page.goto("https://cn.bing.com/search?q=必应上的热点")
        page.wait_for_load_state("networkidle")  # 等待网络空闲

        # 获取页面HTML内容
        html_content = page.content()
        browser.close()

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # 假设热点信息在id为"tob_container"的div中
        hotlist_container = soup.select_one("#tob_container")

        if hotlist_container:
            # 提取所有热点项
            hotlist_items = hotlist_container.select(".tobitem")
            reslut = []
            # 遍历热点项并提取信息
            for item in hotlist_items:
                title = item.select_one(".tobitem_title").text.strip()  # 提取标题
                url = f"https://cn.bing.com/search?q={title}"
                img_url = item.find("img")["src"] if item.find("img") else "No Image"
                reslut.append({"title": title, "url": url, "img_url": img_url})
            return reslut
        else:
            return None
