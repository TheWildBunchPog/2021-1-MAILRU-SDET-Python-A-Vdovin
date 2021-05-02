from dataclasses import dataclass
import faker
from datetime import datetime


fake = faker.Faker()


@dataclass
class Name:
    name_campaign: str = None
    name_segment: str = None


class Builder:

    @staticmethod
    def create_campaign(name_campaign=None):
        if name_campaign is None:
            data = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            name_campaign = fake.lexify(text=f'Новая кампания {data} ??????')

        return Name(name_campaign=name_campaign)

    @staticmethod
    def create_segment(name_segment=None):
        if name_segment is None:
            data = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            name_segment = fake.lexify(text=f'Новый аудиторный сегмент {data} ??????')

        return Name(name_segment=name_segment)
