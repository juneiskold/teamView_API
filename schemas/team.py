from pydantic import BaseModel
from datetime import date

class TeamCreate(BaseModel):
    name: str
    founded_date:date
    home_stadium: str
    coach_name:str


class TeamResponse(TeamCreate):
    id: int

    class Config:
        orm_mode = True