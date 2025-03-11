from fastapi import APIRouter

from models.schemas import HotItem
from services.crawlers.bing import get_bing_hotlist
from services.crawlers.zhihu import ZhihuHotList
from services.crawlers.tieba import TiebaHotList
from services.crawlers.bilibili import BilibiliHotList
from services.crawlers.weibo import WeiboHotList
from services.crawlers.baidu import BaiduHotList

from services.crawlers.codelife import CodeLifeHotList

router = APIRouter()


@router.get("/api/hotlist/bing", response_model=list[HotItem])
async def get_hotlist():
    return await get_bing_hotlist()


@router.get("/api/hotlist/zhihu", response_model=list[HotItem])
async def get_hotlist():
    zhihu = ZhihuHotList()
    try:
        data = await zhihu.get_hot_list()
        return data
    finally:
        await zhihu.close()


@router.get("/api/hotlist/tieba", response_model=list[HotItem])
async def get_hotlist():
    tieba = TiebaHotList()
    try:
        data = await tieba.get_hot_list()
        return data
    finally:
        await tieba.close()


@router.get("/api/hotlist/bilibili", response_model=list[HotItem])
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


@router.get("/api/hotlist/weibo", response_model=list[HotItem])
async def get_hotlist():
    weibo = WeiboHotList()
    try:
        data = await weibo.get_hot_list()
        return data
    finally:
        await weibo.close()


@router.get("/api/hotlist/baidu", response_model=list[HotItem])
async def get_hotlist():
    baidu = BaiduHotList()
    try:
        data = await baidu.get_hot_list()
        return data
    finally:
        await baidu.close()


@router.get("/api/hotlist/douyin", response_model=list[HotItem])
async def get_hotlist():
    douyin = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=DpQvNABoNE"
    )
    try:
        data = await douyin.get_hot_list()
        return data
    finally:
        await douyin.close()
