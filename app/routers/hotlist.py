from fastapi import APIRouter

from models.schemas import HotItem
from services.crawlers.bing import get_bing_hotlist
from services.crawlers.zhihu import get_zhihu_hotlist
from services.crawlers.tieba import get_tieba_hotslist
from services.crawlers.bilibili import get_bilibili_popular, get_bilibili_ranking

router = APIRouter()


@router.get("/api/hotlist/bing", response_model=list[HotItem])
async def get_bing_hotlist():
    return await get_bing_hotlist()


@router.get("/api/hotlist/zhihu", response_model=list[HotItem])
async def get_zhihu_hotlist():
    return await get_zhihu_hotlist()


@router.get("/api/hotlist/tieba", response_model=list[HotItem])
async def get_tieba_hotlist():
    return await get_tieba_hotslist()


@router.get("/api/hotlist/bilibili", response_model=list[HotItem])
async def get_bilibili_hotlist(choice: str = "ranking"):
    if choice == "popular":
        return await get_bilibili_popular()
    else:
        return await get_bilibili_ranking()
