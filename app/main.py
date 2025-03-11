from fastapi import FastAPI
from routers import hotlist

app = FastAPI()
app.include_router(hotlist.router)


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
