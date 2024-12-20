from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.team import TeamCreate, TeamResponse
from models.team import TeamDB
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=TeamResponse, status_code=201)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    db_team = TeamDB(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

# ... (rest of the team endpoints)