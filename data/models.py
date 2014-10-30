from database import Base
from sqlalchemy import Column, Integer, String, Float, BigInteger


class Kodemon(Base):
    __tablename__ = 'kodemon'
    id = Column(Integer, primary_key=True)
    execution_time = Column(Float, nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    token = Column(String, nullable=False)
    key = Column(String, nullable=False)