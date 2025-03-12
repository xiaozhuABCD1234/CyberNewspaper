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


# toutiao
@router.get("/api/hotlist/toutiao", response_model=list[HotItem])
async def get_hotlist():
    toutiao = CodeLifeHotList("https://api.codelife.cc/api/top/list?lang=cn&id=toutiao")
    try:
        data = await toutiao.get_hot_list()
        return data
    finally:
        await toutiao.close()


@router.get("/api/hotlist/weixin", response_model=list[HotItem])
async def get_hotlist():
    weixin = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=WnBe01o371"
    )
    try:
        data = await weixin.get_hot_list()
        return data
    finally:
        await weixin.close()


@router.get("/api/hotlist/36kr", response_model=list[HotItem])
async def get_hotlist():
    kr = CodeLifeHotList("https://api.codelife.cc/api/top/list?lang=cn&id=36kr")
    try:
        data = await kr.get_hot_list()
        return data
    finally:
        await kr.close()


@router.get("/api/hotlist/sspai", response_model=list[HotItem])
async def get_hotlist():
    sspai = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=Y2KeDGQdNP"
    )
    try:
        data = await sspai.get_hot_list()
        return data
    finally:
        await sspai.close()


@router.get("/api/hotlist/huxiu", response_model=list[HotItem])
async def get_hotlist():
    huxiu = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=5VaobgvAj1"
    )
    try:
        data = await huxiu.get_hot_list()
        return data
    finally:
        await huxiu.close()


@router.get("/api/hotlist/ithome", response_model=list[HotItem])
async def get_hotlist():
    ithome = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=74Kvx59dkx"
    )
    try:
        data = await ithome.get_hot_list()
        return data
    finally:
        await ithome.close()


@router.get("/api/hotlist/52pojie", response_model=list[HotItem])
async def get_hotlist():
    pojie = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=NKGoRAzel6"
    )
    try:
        data = await pojie.get_hot_list()
        return data
    finally:
        await pojie.close()


@router.get("/api/hotlist/hupu", response_model=list[HotItem])
async def get_hotlist():
    hupu = CodeLifeHotList("https://api.codelife.cc/api/top/list?lang=cn&id=G47o8weMmN")
    try:
        data = await hupu.get_hot_list()
        return data
    finally:
        await hupu.close()


@router.get("/api/hotlist/newqq", response_model=list[HotItem])
async def get_hotlist():
    newqq = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=12owgX0oNV"
    )
    try:
        data = await newqq.get_hot_list()
        return data
    finally:
        await newqq.close()


@router.get("/api/hotlist/taobao", response_model=list[HotItem])
async def get_hotlist():
    taobao = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=yjvQDpjobg"
    )
    try:
        data = await taobao.get_hot_list()
        return data
    finally:
        await taobao.close()


@router.get("/api/hotlist/juejin", response_model=list[HotItem])
async def get_hotlist():
    juejin = CodeLifeHotList(
        "https://api.codelife.cc/api/top/list?lang=cn&id=QaqeEaVe9R"
    )
    try:
        data = await juejin.get_hot_list()
        return data
    finally:
        await juejin.close()
