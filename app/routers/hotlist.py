from fastapi import APIRouter

from models.schemas import HotItem
from services.crawlers.bing import get_bing_hotlist
from services.crawlers.zhihu import ZhihuHotList
from services.crawlers.tieba import TiebaHotList
from services.crawlers.bilibili import get_bilibili_popular, get_bilibili_ranking
from services.crawlers.weibo import WeiboHotList

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
    if choice == "popular":
        return await get_bilibili_popular()
    else:
        return await get_bilibili_ranking()


@router.get("/api/hotlist/weibo", response_model=list[HotItem])
async def get_hotlist():
    weibo = WeiboHotList()
    try:
        data = await weibo.get_hot_list()
        return data
    finally:
        await weibo.close()
