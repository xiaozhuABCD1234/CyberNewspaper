from fastapi import APIRouter

from models.schemas import HotItem
from services.crawlers.bing import get_bing_hotlist
from services.crawlers.zhihu import get_zhihu_hotlist
from services.crawlers.tieba import get_tieba_hotslist

router = APIRouter()


@router.get("/api/hotlist/bing", response_model=list[HotItem])
async def get_hotlist():
    return await get_bing_hotlist()


@router.get("/api/hotlist/zhihu", response_model=list[HotItem])
async def get_hotlist():
    return await get_zhihu_hotlist()


@router.get("/api/hotlist/tieba", response_model=list[HotItem])
async def get_hotlist():
    return get_tieba_hotslist()
