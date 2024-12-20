from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class PlayerDB(Base):

    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    position = Column(String)
    jersey_number = Column(Integer)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("TeamDB", back_populates="players")
    player_accolades = relationship("AccoladeDB",
                                    primaryjoin="and_(AccoladeDB.recipient_id==PlayerDB.id, "
                                                "AccoladeDB.recipient_type=='Player')")