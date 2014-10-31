from database import Base
from sqlalchemy import Column, Integer, String, Float, BigInteger


class Kodemon(Base):
    __tablename__ = 'kodemon'
    id = Column(Integer, primary_key=True)
    execution_time = Column(Float, nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    token = Column(String, nullable=False)
    key = Column(String, nullable=False)
    func_name = Column(String, nullable=True)
    filename = Column(String, nullable=True)

    def __str__(self):
        # God fucking dam it, look a this mess...
        text = '{ "id": "'
        text += str(self.id)
        text += '", "execution_time": "'
        text += str(self.execution_time)
        text += '", "timestamp": "'
        text += str(self.timestamp)
        text += '", "token": "'
        text += self.token
        text += '", "key": "'
        text += self.key
        text += '", "func_name": "'
        text += self.func_name
        text += '", "filename": "'
        text += self.filename
        text += '" }'

        return text