from dataclasses import dataclass
import faker


fake = faker.Faker()


@dataclass
class Name:
    first_name: str = None
    last_name: str = None


class Builder:

    @staticmethod
    def first_name(first_name=None):
        if first_name is None:
            first_name = fake.first_name()

        return first_name

    @staticmethod
    def last_name(last_name=None):
        if last_name is None:
            last_name = fake.last_name()

        return last_name
