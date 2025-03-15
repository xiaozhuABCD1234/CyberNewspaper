from tortoise import Tortoise, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from models.models import HotItem, Website

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.sqlite",  # 修改为 SQLite 引擎
            "credentials": {
                "file_path": "db.sqlite3",  # SQLite 文件路径
                # "file_path": ":memory:",  # 或用内存数据库
                "journal_mode": "WAL",  # 可选：设置 WAL 模式提升性能
                "busy_timeout": 5,  # 可选：设置超时时间（秒）
                "echo": True,  # 显示执行的 SQL
            },
        }
    },
    "apps": {
        "models": {
            "models": ["models.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
}
