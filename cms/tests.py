import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import resolve, Resolver404, reverse
from django.utils import timezone

from faker import Faker
import pytest

from cms.models import Activity, ActivityType, Record


FAKER_INSTANCE = Faker(['en_US', 'ja_JP'])


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
        record = create_record()
        activity = create_activity(record.id, name='act1')
        assert activity.spent_time == 3600


class ActivityTypeModelTests(TestCase):
    def test_duplicated_activity_type(self):
        """
        [Example] attribute 'name' is duplicated
        """
        name = 'test_activity_type'
        _ = create_activity_type(name=name)
        with self.assertRaises(ValidationError):
            duplicated_act_type = ActivityType(name=name)
            duplicated_act_type.full_clean()


class RecordModelTests(TestCase):
    def test_duplicated_activity_type(self):
        """
        [Example] attribute 'date' is duplicated
        """
        date = datetime.date.today()
        _ = create_record(date=date)
        with self.assertRaises(ValidationError):
            duplicated_record = Record(date=date)
            duplicated_record.full_clean()


class ActivityViewTests(TestCase):
    def test_no_activities(self):
        """
        [Example] If no activities exist, an appropriate message is displayed.
        """
        record = create_record()
        response = self.client.get(reverse('cms:activities', kwargs={'record_id': record.id}))

        assert response.status_code == 200
        self.assertContains(response, "No activities are available.")
        assert response.context['activities'].exists() is False

    def test_with_activities(self):
        """
        [Example] If some activities exist, those records are displayed.
        """
        record = create_record()
        activity1 = create_activity(record.id, name='act1')
        activity2 = create_activity(record.id, name='act2')
        spent_time1 = (activity1.end - activity1.start).seconds / 3600.0
        response = self.client.get(reverse('cms:activities', kwargs={'record_id': record.id}))

        assert response.status_code == 200
        self.assertContains(response, activity1.name)
        self.assertContains(response, activity2.name)

        self.assertContains(response, spent_time1)
        self.assertNotContains(response, "No activities are available.")


class RecordViewTests(TestCase):
    def test_logs(self):
        record = create_record()
        response = self.client.get(reverse('cms:life_logs'))
        self.assertQuerysetEqual(response.context['records'], [record], ordered=False)


def create_record(date=None, comment=None):
    if date is None: date = FAKER_INSTANCE.date_time().date()
    if comment is None: comment = FAKER_INSTANCE.text(max_nb_chars=200)
    return Record.objects.create(date=date, comment=comment)


def create_activity_type(name=None):
    if name is None: name = 'hoge'
    return ActivityType.objects.create(name=name, color='#123456')


def create_activity(record_id, name=None):
    now = timezone.now()
    start = now
    end = now + datetime.timedelta(hours=1)
    spent_time = (end - start).seconds
    return Activity.objects.create(
        record_id=record_id, name=name,
        start=start, end=end, spent_time=spent_time
    )
