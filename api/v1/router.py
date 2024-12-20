from fastapi import APIRouter
from api.v1.endpoints import teams, players, accolades

api_router = APIRouter()

api_router.include_router(teams.router, prefix="/teams", tags=["teams"])
# api_router.include_router(players.router, tags=["players"])
# api_router.include_router(accolades.router, tags=["accolades"])