from mysql.models import *
from utils.builder import Builder


builder = Builder()


class MySQLBuilder:
    def __init__(self, client):
        self.client = client

    def add_user(self, access=True):
        if access:
            right = 1
        else:
            right = 0
        user = TestUsers(
            username=builder.login(),
            password=builder.password(),
            email=builder.email(),
            access=right
        )
        self.client.session.add(user)
        self.client.session.commit()
        return user

    def get_user(self, username):
        res = self.client.session.query(TestUsers).filter_by(username=username).all()[0]
        self.client.session.expire_all()
        return {'username': res.username, 'email': res.email, 'password': res.password, 'active': res.active,
                'access': res.access, 'start_active_time': res.start_active_time}

    def delete_user(self, ident):
        res = self.client.session.query(TestUsers).filter_by(id=ident)
        res.delete()
        self.client.session.commit()
