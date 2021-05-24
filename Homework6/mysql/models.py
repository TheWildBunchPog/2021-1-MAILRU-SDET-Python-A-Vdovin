from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalRequests(Base):
    __tablename__ = 'total_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TotalRequests(" \
               f"count='{self.count}'," \
               f")>"

    count = Column(Integer, nullable=False, primary_key=True)


class TotalRequestsByType(Base):
    __tablename__ = 'total_requests_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TotalRequestsByType(" \
               f"type='{self.type}'," \
               f"count='{self.count}'," \
               f")>"

    type = Column(String(500), nullable=False, primary_key=True)
    count = Column(Integer, nullable=False)


class TopMostFrequentQueries(Base):
    __tablename__ = 'top_most_frequent_queries'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TopMostFrequentQueries(" \
               f"url='{self.url}'," \
               f"count='{self.count}'," \
               f")>"

    url = Column(String(500), nullable=False, primary_key=True)
    count = Column(Integer, nullable=False)


class TopRequestsBySizeWithClientError(Base):
    __tablename__ = 'top_requests_by_size_with_client_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TopRequestsBySizeWithClientError(" \
               f"url='{self.url}'," \
               f"status_code='{self.status_code}'," \
               f"size='{self.size}'," \
               f"ip='{self.ip}'," \
               f")>"

    url = Column(String(500), nullable=False, primary_key=True)
    status_code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(30), nullable=False)


class TopUsersByNumberRequestsWithServerError(Base):
    __tablename__ = 'top_users_by_number_requests_with_server_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TopRequestsBySizeWithClientError(" \
               f"ip='{self.ip}'," \
               f"count='{self.count}'," \
               f")>"

    ip = Column(String(30), nullable=False, primary_key=True)
    count = Column(Integer, nullable=False)
