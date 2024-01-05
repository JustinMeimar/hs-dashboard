from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase
from typing import Optional

class Base(DeclarativeBase):
    pass

# Define the Log model
class Log(Base):
    __tablename__ = 'logs'

    ip: Optional[str]               = Column(String(255), primary_key=True)
    datetime: Optional[DateTime]    = Column(DateTime, primary_key=True)
    request_method: Optional[str]   = Column(String(50))
    path: Optional[str]             = Column(Text)
    status: Optional[int]           = Column(Integer)
    size: Optional[int]             = Column(Integer)
    referrer: Optional[str]         = Column(Text)
    user_agent: Optional[str]       = Column(Text)