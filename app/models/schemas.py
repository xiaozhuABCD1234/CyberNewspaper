from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class HotItem(BaseModel):
    title: str
    url: HttpUrl
    heat: str | int | None = None
    description: str | None = None
    image: HttpUrl | str | None = None
    author: str | None = None
