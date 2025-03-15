# main.py
from fastapi import FastAPI
from routers import hotlist
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from core.database import TORTOISE_ORM

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5173/",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    # # 如果数据库为空，则自动生成对应表单，生产环境不要开
    add_exception_handlers=True,
    # # 生产环境不要开，会泄露调试信息
)
app.include_router(hotlist.router)


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
