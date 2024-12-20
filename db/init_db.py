from datetime import date
from sqlalchemy.orm import Session
from models.team import TeamDB
from models.player import PlayerDB
from models.accolade import AccoladeDB
from .session import engine, SessionLocal
from models.base import Base

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # checking if we already have data
    if db.query(TeamDB).first():
        db.close()
        return

