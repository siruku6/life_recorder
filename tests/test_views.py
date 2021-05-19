from faker import Faker

from django.test import TestCase
from django.urls import reverse

from cms.models import Record, TemplateActivity
from cms.views import create_template_activity
from tests.factories import *


FAKER_INSTANCE = Faker(['en_US', 'ja_JP'])


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
    def test_today_record_exists(self):
        self.client.get(reverse('cms:life_logs'))

        today: datetime = datetime.date.today()
        dates = Record.objects.values_list('date', flat=True)
        self.assertIn(today, dates)

    def test_created_record_shown(self):
        record: Record = RecordFactory()

        response = self.client.get(reverse('cms:life_logs'))
        self.assertIn(record, response.context['records'])
        assert len(response.context['records']) == 2
