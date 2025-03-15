from fastapi import APIRouter

from models.schemas import HotItemShow
from services.crawlers.bing import get_bing_hotlist
from services.crawlers.zhihu import ZhihuHotList
from services.crawlers.tieba import TiebaHotList
from services.crawlers.bilibili import BilibiliHotList
from services.crawlers.weibo import WeiboHotList
from services.crawlers.baidu import BaiduHotList

from services.crawlers.codelife import CodeLifeHotList

router = APIRouter()


@router.get(
    "/api/hotlist/now/bing",
    response_model=list[HotItemShow],
    summary="获取 Bing 实时搜索热门列表",
    description="从 Bing 搜索引擎获取当前实时热门搜索关键词列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    return await get_bing_hotlist()


@router.get(
    "/api/hotlist/now/zhihu",
    response_model=list[HotItemShow],
    summary="获取知乎实时热门话题列表",
    description="从知乎热榜获取当前实时热门话题列表，返回包含标题、链接、热度和讨论量的热门条目。",
)
async def get_hotlist():
    zhihu = ZhihuHotList()
    try:
        data = await zhihu.get_hot_list()
        return data
    finally:
        await zhihu.close()


@router.get(
    "/api/hotlist/now/tieba",
    response_model=list[HotItemShow],
    summary="获取百度贴吧实时热门帖子列表",
    description="从百度贴吧获取当前实时热门帖子列表，返回包含标题、链接、回复数和热度的热门条目。",
)
async def get_hotlist():
    tieba = TiebaHotList()
    try:
        data = await tieba.get_hot_list()
        return data
    finally:
        await tieba.close()


@router.get(
    "/api/hotlist/now/bilibili",
    response_model=list[HotItemShow],
    summary="获取 B 站热门视频列表",
    description="从 B 站获取热门视频列表，可通过 `choice` 参数选择返回类型：`ranking`（默认，热门排行榜）或 `popular`（实时热门推荐视频）。返回包含标题、链接、播放量和热度的热门条目。",
)
async def get_hotlist(choice: str = "ranking"):
    bilibili = BilibiliHotList()
    try:
        if choice == "popular":
            data = await bilibili.get_bilibili_popular()
        else:
            data = await bilibili.get_bilibili_ranking()
        return data
    finally:
        await bilibili.close()


@router.get(
    "/api/hotlist/now/weibo",
    response_model=list[HotItemShow],
    summary="获取微博实时热门话题列表",
    description="从微博热榜获取当前实时热门话题列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    weibo = WeiboHotList()
    try:
        data = await weibo.get_hot_list()
        return data
    finally:
        await weibo.close()


@router.get(
    "/api/hotlist/now/baidu",
    response_model=list[HotItemShow],
    summary="获取百度实时热门搜索列表",
    description="从百度搜索获取当前实时热门搜索关键词列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    baidu = BaiduHotList()
    try:
        data = await baidu.get_hot_list()
        return data
    finally:
        await baidu.close()


@router.get(
    "/api/hotlist/now/douyin",
    response_model=list[HotItemShow],
    summary="获取抖音实时热门话题列表",
    description="从抖音热榜获取当前实时热门话题列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    douyin = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=DpQvNABoNE"
    )
    try:
        data = await douyin.get_hot_list()
        return data
    finally:
        await douyin.close()


@router.get(
    "/api/hotlist/now/toutiao",
    response_model=list[HotItemShow],
    summary="获取头条实时热门话题列表",
    description="从头条热榜获取当前实时热门话题列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    toutiao = CodeLifeHotList("https://api.codelife.cc/api/top/list?lang=cn&id=toutiao")
    try:
        data = await toutiao.get_hot_list()
        return data
    finally:
        await toutiao.close()


@router.get(
    "/api/hotlist/now/weixin",
    response_model=list[HotItemShow],
    summary="获取微信实时热门文章列表",
    description="从微信热文获取当前实时热门文章列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    weixin = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=WnBe01o371"
    )
    try:
        data = await weixin.get_hot_list()
        return data
    finally:
        await weixin.close()


@router.get(
    "/api/hotlist/now/36kr",
    response_model=list[HotItemShow],
    summary="获取 36 氪实时热门文章列表",
    description="从 36 氪获取当前实时热门文章列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    kr = CodeLifeHotList("https://api.codelife.cc/api/top/list?lang=cn&id=36kr")
    try:
        data = await kr.get_hot_list()
        return data
    finally:
        await kr.close()


@router.get(
    "/api/hotlist/now/sspai",
    response_model=list[HotItemShow],
    summary="获取少数派实时热门文章列表",
    description="从少数派获取当前实时热门文章列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    sspai = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=Y2KeDGQdNP"
    )
    try:
        data = await sspai.get_hot_list()
        return data
    finally:
        await sspai.close()


@router.get(
    "/api/hotlist/now/huxiu",
    response_model=list[HotItemShow],
    summary="获取虎嗅实时热门文章列表",
    description="从虎嗅获取当前实时热门文章列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    huxiu = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=5VaobgvAj1"
    )
    try:
        data = await huxiu.get_hot_list()
        return data
    finally:
        await huxiu.close()


@router.get(
    "/api/hotlist/now/ithome",
    response_model=list[HotItemShow],
    summary="获取 IT 之家实时热门新闻列表",
    description="从 IT 之家获取当前实时热门新闻列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    ithome = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=74Kvx59dkx"
    )
    try:
        data = await ithome.get_hot_list()
        return data
    finally:
        await ithome.close()


@router.get(
    "/api/hotlist/now/52pojie",
    response_model=list[HotItemShow],
    summary="获取吾爱破解实时热门资源列表",
    description="从吾爱破解获取当前实时热门资源列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    pojie = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=NKGoRAzel6"
    )
    try:
        data = await pojie.get_hot_list()
        return data
    finally:
        await pojie.close()


@router.get(
    "/api/hotlist/now/hupu",
    response_model=list[HotItemShow],
    summary="获取虎扑实时热门帖子列表",
    description="从虎扑社区获取当前实时热门帖子列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    hupu = CodeLifeHotList("https://api.codelife.cc/api/top/list?lang=cn&id=G47o8weMmN")
    try:
        data = await hupu.get_hot_list()
        return data
    finally:
        await hupu.close()


@router.get(
    "/api/hotlist/now/newqq",
    response_model=list[HotItemShow],
    summary="获取腾讯新闻实时热门话题列表",
    description="从腾讯新闻获取当前实时热门话题列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    newqq = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=12owgX0oNV"
    )
    try:
        data = await newqq.get_hot_list()
        return data
    finally:
        await newqq.close()


@router.get(
    "/api/hotlist/now/taobao",
    response_model=list[HotItemShow],
    summary="获取淘宝实时热门商品列表",
    description="从淘宝获取当前实时热门商品列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    taobao = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=yjvQDpjobg"
    )
    try:
        data = await taobao.get_hot_list()
        return data
    finally:
        await taobao.close()


@router.get(
    "/api/hotlist/now/juejin",
    response_model=list[HotItemShow],
    summary="获取掘金实时热门文章列表",
    description="从掘金获取当前实时热门文章列表，返回包含标题、链接和热度的热门条目。",
)
async def get_hotlist():
    juejin = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=QaqeEaVe9R"
    )
    try:
        data = await juejin.get_hot_list()
        return data
    finally:
        await juejin.close()
