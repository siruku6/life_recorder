import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import resolve, Resolver404, reverse
from django.utils import timezone

from faker import Faker
import pytest

from cms.models import Activity, ActivityType, Record, TemplateActivity
from cms.views import create_template_activity


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
        record = factory_create_record()
        activity = factory_create_activity(record.id, name='act1')
        assert activity.spent_time == 3600


class ActivityTypeModelTests(TestCase):
    def test_duplicated_activity_type(self):
        """
        [Example] attribute 'name' is duplicated
        """
        name = 'test_activity_type'
        _ = factory_create_activity_type(name=name)
        with self.assertRaises(ValidationError):
            duplicated_act_type = ActivityType(name=name)
            duplicated_act_type.full_clean()


class RecordModelTests(TestCase):
    def test_duplicated_activity_type(self):
        """
        [Example] attribute 'date' is duplicated
        """
        date = datetime.date.today()
        _ = factory_create_record(date=date)
        with self.assertRaises(ValidationError):
            duplicated_record = Record(date=date)
            duplicated_record.full_clean()


class ActivityViewTests(TestCase):
    """ ActivityView """
    def test_no_activities(self):
        """
        [Example] If no activities exist, an appropriate message is displayed.
        """
        record = factory_create_record()
        response = self.client.get(reverse('cms:activities', kwargs={'record_id': record.id}))

        assert response.status_code == 200
        self.assertContains(response, "No activities are available.")
        assert response.context['activities'].exists() is False

    def test_with_activities(self):
        """
        [Example] If some activities exist, those records are displayed.
        """
        record = factory_create_record()
        activity1 = factory_create_activity(record.id, name='act1')
        activity2 = factory_create_activity(record.id, name='act2')
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
        act_type = factory_create_activity_type()
        tmp_act = create_template_activity({
            'name': FAKER_INSTANCE.text(max_nb_chars=255),
            'activity_type': act_type.id
        })
        assert TemplateActivity.objects.first() == tmp_act

    def test_update_template_activity(self):
        """
        [Example] update activity_type_id of a template_activity.
        """
        act_type1 = factory_create_activity_type()
        act_type2 = factory_create_activity_type()
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
        record = factory_create_record()
        response = self.client.get(reverse('cms:life_logs'))
        self.assertQuerysetEqual(response.context['records'], [record], ordered=False)


def factory_create_record(date: datetime.date = None, comment: str = None) -> Record:
    if date is None: date = FAKER_INSTANCE.date_time().date()
    if comment is None: comment = FAKER_INSTANCE.text(max_nb_chars=200)
    return Record.objects.create(date=date, comment=comment)


def factory_create_activity_type(name: str = None) -> ActivityType:
    if name is None: name = 'hoge'
    return ActivityType.objects.create(name=name, color='#123456')


def factory_create_activity(record_id: int, name: str = None) -> Activity:
    now = timezone.now()
    start = now
    end = now + datetime.timedelta(hours=1)
    spent_time = (end - start).seconds
    return Activity.objects.create(
        record_id=record_id, name=name,
        start=start, end=end, spent_time=spent_time
    )
