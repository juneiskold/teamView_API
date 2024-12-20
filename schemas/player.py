from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str
    age: int
    position: str
    jersey_number: int


class PlayerResponse(PlayerCreate):
    id: int
    team_id: int

    class Config:
        orm_mode = True