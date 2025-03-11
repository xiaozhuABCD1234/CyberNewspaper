from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import asyncio


async def get_bing_hotlist() -> list[dict]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # 打开浏览器
        context = await browser.new_context()
        page = await context.new_page()

        # 打开目标网页并等待加载完成
        await page.goto("https://cn.bing.com/search?q=必应上的热点")
        await page.wait_for_load_state("networkidle")  # 等待网络空闲

        # 获取页面HTML内容
        html_content = await page.content()
        await browser.close()

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # 假设热点信息在id为"tob_container"的div中
        hotlist_container = soup.select_one("#tob_container")

        if hotlist_container:
            # 提取所有热点项
            hotlist_items = hotlist_container.select(".tobitem")
            result = []
            # 遍历热点项并提取信息
            for item in hotlist_items:
                title = item.select_one(".tobitem_title").text.strip()  # 提取标题
                url = f"https://cn.bing.com/search?q={title}"  # 构造搜索链接
                image = item.find("img")["src"] if item.find("img") else "No Image"
                result.append({"title": title, "url": url, "img_url": image})
            return result
        else:
            return None
