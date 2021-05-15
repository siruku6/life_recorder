import datetime
import pytz
import factory
from faker import Faker

from cms.models import *


FAKER_INSTANCE = Faker(['en_US', 'ja_JP'])


class RecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Record
    date = FAKER_INSTANCE.date_time().date()
    comment = FAKER_INSTANCE.text(max_nb_chars=200)


class ActivityTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityType
    name = factory.Sequence(lambda n: '{}-{}'.format(FAKER_INSTANCE.unique.word(), n))
    color = '#123456'


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Activity
    record = factory.SubFactory(RecordFactory)
    name = FAKER_INSTANCE.unique.word()
    start = FAKER_INSTANCE.unique.date_time(pytz.timezone('Asia/Tokyo'))
    end = start + datetime.timedelta(minutes=30)
    spent_time = (end - start).seconds
