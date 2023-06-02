from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base


Base = declarative_base()
# class Base(declarative_base):
#     pass

class Waiters(Base):
    __tablename__ = "waiters"

    waiter_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), default="Smith")
    age = Column(Integer)
