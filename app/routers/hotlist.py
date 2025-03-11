from fastapi import APIRouter
from models.schemas import HotList
from services.crawlers.bing import get_bing_hotlist
from services.crawlers.zhihu import get_zhihu_hotlist


router = APIRouter()


@router.get("/api/hotlist/bing")
async def get_hotlist():
    return await get_bing_hotlist()


@router.get("/api/hotlist/zhihu")
async def get_hotlist():
    return await get_zhihu_hotlist()
