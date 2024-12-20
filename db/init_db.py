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

    # pre-recorded teams
    teams_data = [
        {
            "name": "Manchester United",
            "founded_date": date(1878, 1, 1),
            "home_stadium": "Old Trafford",
            "coach_name": "Ruben Amorim"
        },

        {
            "name": "Real Madrid Club de Futbol",
            "founded_date": date(1902, 3, 6),
            "home_stadium": "Estadio Santiago Bernabeu",
            "coach_name": "Carlo Ancelotti"
        }
    ]

    teams = []

    for team_data in teams_data:
        team = TeamDB(**team_data)
        db.add(team)
        db.flush()
        teams.append(team)