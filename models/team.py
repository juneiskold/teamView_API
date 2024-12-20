from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base

class TeamDB(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    founded_date = Column(Date)
    home_stadium = Column(String)
    coach_name = Column(String)

    players = relationship("PlayerDB", back_populates="team")
    team_accolades = relationship("AccoladeDB",
                                  primaryjoin="and_(AccoladeDB.recipient_id==TeamDB.id, "
                                              "AccoladeDB.recipient_type=='Team')")