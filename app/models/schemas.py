# models/schemas.py
from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class HotItemShow(BaseModel):
    title: str
    url: HttpUrl
    heat: str | int | None = None
    description: str | None = None
    author: str | None = None
