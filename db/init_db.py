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

    # Players data
    players_data = [
        {
            "name": "Bruno Fernandes",
            "age": 28,
            "position": "Midfielder",
            "jersey_number": 8,
            "team_id": teams[0].id
        },

        {
            "name": "Luka Modric",
            "age": 39,
            "position": "Midfielder",
            "jersey_number": 10,
            "team_id": teams[1].id
        }
    ]

    players = []
    for players_data in players_data:
        player = PlayerDB(**players_data)
        db.add(player)
        db.flush()
        players.append(player)


    # accolade data
    accolades_data = [
        {
            "title": "Premier League Championship",
            "description": "2022/23 Season Winners",
            "date_awarded": date(2023, 5, 28),
            "recipient_type": "Team",
            "recipient_id": teams[0].id
        },

        {
            "title": "Golden Boot",
            "description": "Top Scorer of the Season",
            "date_awarded": date(2023, 5, 28),
            "recipient_type": "Player",
            "recipient_id": players[0].id
        }
    ]

    for accolade_data in accolades_data:
        accolade = AccoladeDB(**accolade_data)
        db.add(accolade)

    db.commit()
    db.close()