import datetime
from django.test import TestCase

from cms.models import Record
from cms.forms import RecordForm
from tests.factories import *


class RecordFormTests(TestCase):
    def test_validation_of_comment(self):
        """
        [Example] the length of attribute 'comment' is more than 255
        """
        params: dict = {'date': datetime.date.today(), 'comment': 'test,' * 52}
        record: Record = RecordFactory()
        form: RecordForm = RecordForm(params, instance=record)
        self.assertFalse(form.is_valid())
        assert 'Please input less than 255 characters' in form.errors['comment']

    def test_can_update_existing_record(self):
        """
        [Example] only comment is going to be updated
        """
        # Create original record
        original_commnet: str = 'existing record'
        params: dict = {'date': datetime.date.today(), 'comment': original_commnet}
        record: Record = RecordFactory(**params)

        # Updating instance of record
        new_comment: str = 'changed'
        params['comment'] = new_comment
        form: RecordForm = RecordForm(params, instance=record)
        assert form.is_valid() is True
        assert Record.objects.all()[0].comment == original_commnet

        # Update record
        record: Record = form.save()
        assert record.comment == new_comment
