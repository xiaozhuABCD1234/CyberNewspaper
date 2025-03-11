from pydantic import BaseModel, HttpUrl


class HotItem(BaseModel):
    title: str
    url: HttpUrl
    heat: str | None
    description: str | None
    image: HttpUrl | None
    author: str | None


class HotList(BaseModel):
    items: list[HotItem]
