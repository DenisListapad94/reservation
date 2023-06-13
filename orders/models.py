from sqlalchemy import Integer, String, Column, TIMESTAMP, ForeignKey
from database import Base


class Waiters(Base):
    __tablename__ = "waiters"

    waiter_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), default="Smith")
    age = Column(Integer)

    def get_info_person(self):
        return f"{self.name} {self.age}"


class TableReservation(Base):
    __tablename__ = "tables"
    table_id = Column(Integer, primary_key=True)
    start_armor = Column(TIMESTAMP)
    end_armor = Column(TIMESTAMP)
    waiter = Column(Integer, ForeignKey("waiters.waiter_id"))

# with Session(engine) as session:
#     waiter_1 = Waiters(name="Mark",last_name="Parker",age=38)
#     waiter_2 = Waiters(name="Anna", last_name="Gerasimenya", age=21)
#     waiter_3 = Waiters(name="Naik", last_name="Walter", age=25)
#     session.add_all([waiter_1,waiter_2,waiter_3])
#     session.commit()

# with Session(engine) as session:
#     waiters = session.query(Waiters.name,Waiters.age).all()
#     for waiter in waiters:
#         print(waiter.name,waiter.age)

# with Session(engine) as session:
#     waiters = session.query(Waiters.name,Waiters.age).filter((Waiters.age>=25)& (Waiters.age<=30))
#     for waiter in waiters:
#         print(waiter.name,waiter.age)
#
# with Session(engine) as session:
#     waiters = session.query(Waiters.name,Waiters.age).filter(Waiters.last_name=="Parker").order_by(Waiters.age)
#     for waiter in waiters:
#         print(waiter.name,waiter.age)

# with Session(engine) as session:
#     waiters = session.query(Waiters).filter(Waiters.age>=10).order_by(-Waiters.age).limit(4).offset(2)
#     for waiter in waiters:
#         print(waiter.name,waiter.age)

# with Session(engine) as session:
#     waiter = session.query(Waiters).filter(Waiters.waiter_id==7).first()
#     session.delete(waiter)
#     session.commit()

# delete from add

# with Session(engine) as session:
#     from random import  randint
#     for _ in range(20):
#         table = TableReservation(waiter=random.randint(1,6))
#         session.add(table)
#         session.commit()

# TODO group_by
# with Session(engine) as session:
#     # waiter_tables_count = session.query(TableReservation).join(Waiters).group_by(Waiters.waiter_id)
#     waiter_tables_count = session.query(TableReservation.table_id,
#                   func.count(Waiters.waiter_id)).group_by(Waiters.waiter_id).all()
#     for table in waiter_tables_count:
#         print(table)
