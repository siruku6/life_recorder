import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import resolve, Resolver404
from django.utils import timezone

from cms.models import Activity

import pytest

from cms.models import ActivityType, Record
from tests.factories import *


class UrlTest(TestCase):
    def test_not_exist_url(self):
        with pytest.raises(Resolver404):
            resolve('/cms/hoge/')

    def test_index_url(self):
        result = resolve('/cms/')
        assert result.url_name == 'index'

    def test_exist_url(self):
        result = resolve('/cms/logs/')
        assert result.url_name == 'life_logs'


class ActivityModelTests(TestCase):
    def test_spent_time_is_set(self):
        """
        [Example] attribute 'spent_time' is always automatically set
        """
        activity = factory_create_activity(name='act1')
        assert activity.spent_time == 3600


class ActivityTypeModelTests(TestCase):
    def test_duplicated_activity_type(self):
        """
        [Example] attribute 'name' is duplicated
        """
        name = 'test_activity_type'
        _ = ActivityTypeFactory(name=name)
        with self.assertRaises(ValidationError):
            duplicated_act_type = ActivityType(name=name)
            duplicated_act_type.full_clean()


class RecordModelTests(TestCase):
    def test_duplicated_date(self):
        """
        [Example] attribute 'date' is duplicated
        """
        date = datetime.date.today()
        _ = RecordFactory(date=date)
        with self.assertRaises(ValidationError):
            duplicated_record = Record(date=date)
            duplicated_record.full_clean()


def factory_create_activity(name: str = None) -> Activity:
    record = RecordFactory()
    now = timezone.localtime()
    start = now
    end = now + datetime.timedelta(hours=1)
    spent_time = (end - start).seconds
    return Activity.objects.create(
        record_id=record.id, name=name,
        start=start, end=end, spent_time=spent_time
    )
