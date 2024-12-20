from fastapi import FastAPI
from uvloop.handles.async_ import async_

from api.v1.router import api_router
from db.init_db import init_db

app = FastAPI(title="Football API", description="Manage football teams, players and accolades")


# include routers
app.include_router(api_router, prefix="/api/v1")

# initialize database with pre-recorded data
@app.on_event("startup")
async def startup_event():
    init_db()



# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
