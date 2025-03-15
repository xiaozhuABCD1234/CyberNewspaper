# utils/converters.py
from models.models import HotItem, Website
from models.schemas import HotItemShow
from utils.utils import get_website_name_from_show, get_website_url_from_show


def convert_db_to_show(hot_item: HotItem) -> HotItemShow:
    return HotItemShow(
        title=hot_item.title,
        url=hot_item.url,
        heat=hot_item.heat,
        description=hot_item.description,
        author=hot_item.author,
    )


def convert_show_to_db(show_item: HotItemShow) -> HotItem:
    website = Website(
        name=get_website_name_from_show(show_item),
        url=get_website_url_from_show(show_item),
    )

    return HotItem(
        title=show_item.title,
        url=str(show_item.url),
        heat=show_item.heat,
        description=show_item.description,
        author=show_item.author,
        source=website,
    )
