import datetime

from django.test import TestCase
from django.urls import resolve, Resolver404, reverse
from django.utils import timezone
import pytest

from .models import Activity, Record


class HomePageTest(TestCase):
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


def create_record(date=None, comment=None):
    if date is None: date = timezone.now()
    return Record.objects.create(date=date, comment=comment)


def create_activity(record_id, name=None):
    now = timezone.now()
    start = now
    end = now + datetime.timedelta(hours=1)
    spent_time = (end - start).seconds
    return Activity.objects.create(
        record_id=record_id, name=name,
        start=start, end=end, spent_time=spent_time
    )
