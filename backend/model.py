from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase
from typing import Optional

class Base(DeclarativeBase):
    pass

# Define the Log model
class Log(Base):
    __tablename__ = 'logs'

    id: int                         = Column(Integer, primary_key=True)
    ip: Optional[str]               = Column(String(255))
    datetime: Optional[DateTime]    = Column(DateTime)
    request_method: Optional[str]   = Column(String(50))
    path: Optional[str]             = Column(Text)
    status: Optional[int]           = Column(Integer)
    size: Optional[int]             = Column(Integer)
    referrer: Optional[str]         = Column(Text)
    user_agent: Optional[str]       = Column(Text)