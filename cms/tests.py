from django.test import TestCase
from django.urls import resolve, Resolver404, reverse
from django.utils import timezone
import pytest

from .models import Record


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


def create_record(date=None, comment=None):
    if date is None: date = timezone.now()
    return Record.objects.create(date=date, comment=comment)
