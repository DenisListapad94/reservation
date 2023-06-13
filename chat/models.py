from sqlalchemy import Integer, String, Column
from database import Base


class Message(Base):
    __tablename__ = "message"

    message_id = Column(Integer, primary_key=True)
    message = Column(String(100))
