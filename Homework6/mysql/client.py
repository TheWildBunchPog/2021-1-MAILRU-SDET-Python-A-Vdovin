import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from models import Base


class MysqlClient:
    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine,
                                    autocommit=False,  # use autocommit on session.add
                                    expire_on_commit=False  # expire model after commit (requests data from database)
                                    )()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def recreate_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()

    def create_total_requests(self):
        if not inspect(self.engine).has_table('total_requests'):
            Base.metadata.tables['total_requests'].create(self.engine)

    def create_total_requests_by_type(self):
        if not inspect(self.engine).has_table('total_requests_by_type'):
            Base.metadata.tables['total_requests_by_type'].create(self.engine)

    def create_top_most_frequent_queries(self):
        if not inspect(self.engine).has_table('top_most_frequent_queries'):
            Base.metadata.tables['top_most_frequent_queries'].create(self.engine)

    def create_top_requests_by_size_with_client_error(self):
        if not inspect(self.engine).has_table('top_requests_by_size_with_client_error'):
            Base.metadata.tables['top_requests_by_size_with_client_error'].create(self.engine)

    def create_top_users_by_number_requests_with_server_error(self):
        if not inspect(self.engine).has_table('top_users_by_number_requests_with_server_error'):
            Base.metadata.tables['top_users_by_number_requests_with_server_error'].create(self.engine)
