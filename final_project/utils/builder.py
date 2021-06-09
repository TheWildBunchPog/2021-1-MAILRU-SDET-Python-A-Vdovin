from dataclasses import dataclass
import faker


fake = faker.Faker()


@dataclass
class Name:
    login: str = None
    email: str = None
    password: str = None


class Builder:

    @staticmethod
    def login(login=None):
        if login is None:
            login = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)

        return login

    @staticmethod
    def email(email=None):
        if email is None:
            email = fake.email()

        return email

    @staticmethod
    def password(password=None):
        if password is None:
            password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

        return password
