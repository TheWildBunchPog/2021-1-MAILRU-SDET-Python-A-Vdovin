from sqlalchemy import Column, Integer, String, SmallInteger, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestUsers(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TestUsers(" \
               f"id='{self.id}'," \
               f"username='{self.username}', " \
               f"password='{self.password}', " \
               f"email='{self.email}'" \
               f"access='{self.access}'" \
               f"active='{self.active}'" \
               f"start_active_time='{self.start_active_time}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    access = Column(SmallInteger, nullable=True, default=0)
    active = Column(SmallInteger, nullable=True, default=0)
    start_active_time = Column(Date, nullable=True)
