from django.forms import ModelForm
from cms.models import Record


class RecordForm(ModelForm):
    """活動記録のフォーム"""
    class Meta:
        model = Record
        fields = ('date', 'comment', )
