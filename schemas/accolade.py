from pydantic import BaseModel
from datetime import date


class AccoladeCreate(BaseModel):
    title: str
    description: str
    date_awarded: date


class AccoladeResponse(AccoladeCreate):
    id: int
    recipient_type: str
    recipient_id: int

    class Config:
        orm_mode = True