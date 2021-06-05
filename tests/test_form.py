import datetime
from django.test import TestCase

from cms.models import Record
from cms.forms import RecordForm


class RecordFormTests(TestCase):
    def test_validation_of_comment(self):
        """
        [Example] the length of attribute 'comment' is more than 255
        """
        params = {'date': datetime.date.today(), 'comment': 'test,' * 52}
        record = Record()
        form = RecordForm(params, instance=record)
        self.assertFalse(form.is_valid())
        assert 'Please input less than 255 characters' in form.errors['comment']
