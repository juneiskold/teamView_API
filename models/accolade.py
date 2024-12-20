from sqlalchemy import Column, Integer, String, Date
from .base import Base

class AccoladeDB(Base):
    __tablename__ = "accolades"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date_awarded = Column(Date)
    recipient_type = Column(String)
    recipient_id = Column(Integer)