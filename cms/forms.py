from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput  # , TimePickerInput, DateTimePickerInput
from cms.models import Record


class RecordForm(ModelForm):
    """活動記録のフォーム"""
    class Meta:
        model = Record
        fields = ('date', 'comment', )
        widgets = {
            'date': DatePickerInput(
                format='%Y-%m-%d',
                # options={
                #     'locale': 'ja',
                #     'dayViewHeaderFormat': 'YYYY年 MMMM',
                # }
            ),
        }
