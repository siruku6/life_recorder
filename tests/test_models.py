import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import resolve, Resolver404, reverse
from django.utils import timezone

from faker import Faker
import pytest

from cms.models import Activity, ActivityType, Record, TemplateActivity
from cms.views import create_template_activity
from tests.factories import *


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
    def test_duplicated_activity_type(self):
        """
        [Example] attribute 'date' is duplicated
        """
        date = datetime.date.today()
        _ = RecordFactory(date=date)
        with self.assertRaises(ValidationError):
            duplicated_record = Record(date=date)
            duplicated_record.full_clean()


class ActivityViewTests(TestCase):
    """ ActivityView """
    def test_no_activities(self):
        """
        [Example] If no activities exist, an appropriate message is displayed.
        """
        record = RecordFactory()
        response = self.client.get(reverse('cms:activities', kwargs={'record_id': record.id}))

        assert response.status_code == 200
        self.assertContains(response, "No activities are available.")
        assert response.context['activities'].exists() is False

    def test_with_activities(self):
        """
        [Example] If some activities exist, those records are displayed.
        """
        record = RecordFactory()
        activity1 = ActivityFactory(record=record, name='act1')
        activity2 = ActivityFactory(record=record, name='act2')

        spent_time1 = (activity1.end - activity1.start).seconds / 3600.0
        response = self.client.get(reverse('cms:activities', kwargs={'record_id': record.id}))

        assert response.status_code == 200
        self.assertContains(response, activity1.name)
        self.assertContains(response, activity2.name)

        self.assertContains(response, spent_time1)
        self.assertNotContains(response, "No activities are available.")

    def test_create_template_activity_once(self):
        """
        [Example] create a template_activity.
        """
        act_type = ActivityTypeFactory()
        tmp_act = create_template_activity({
            'name': FAKER_INSTANCE.text(max_nb_chars=255),
            'activity_type': act_type.id
        })
        assert TemplateActivity.objects.first() == tmp_act

    def test_update_template_activity(self):
        """
        [Example] update activity_type_id of a template_activity.
        """
        act_type1 = ActivityTypeFactory()
        act_type2 = ActivityTypeFactory()
        tmp_act_name = FAKER_INSTANCE.sentence()

        tmp_act1 = create_template_activity({
            'name': tmp_act_name,
            'activity_type': act_type1.id
        })
        tmp_act2 = create_template_activity({
            'name': tmp_act_name,
            'activity_type': act_type2.id
        })
        first_temp_act = TemplateActivity.objects.first()
        assert first_temp_act.activity_type_id != tmp_act1.activity_type_id
        assert first_temp_act.activity_type_id == tmp_act2.activity_type_id


class RecordViewTests(TestCase):
    def test_logs(self):
        record = RecordFactory()
        response = self.client.get(reverse('cms:life_logs'))
        self.assertQuerysetEqual(response.context['records'], [record], ordered=False)


def factory_create_activity(name: str = None) -> Activity:
    record = RecordFactory()
    now = timezone.now()
    start = now
    end = now + datetime.timedelta(hours=1)
    spent_time = (end - start).seconds
    return Activity.objects.create(
        record_id=record.id, name=name,
        start=start, end=end, spent_time=spent_time
    )
