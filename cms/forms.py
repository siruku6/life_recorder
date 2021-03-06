from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput  # , DateTimePickerInput
from cms.models import Record, Activity


class RecordForm(ModelForm):
    """活動日のフォーム"""
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


class ActivityForm(ModelForm):
    """活動内容のフォーム"""
    # TODO: activity_type は、選択式のみでなく、入力も可能にする
    #   https://stackoverflow.com/questions/24783275/django-form-with-choices-but-also-with-freetext-option
    #   https://teratail.com/questions/201160
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    class Meta():
        model = Activity
        fields = ('activity_type', 'name', 'start', 'end', )
        widgets = {
            'start': TimePickerInput(
                options={
                    "format": 'HH:mm',
                    "stepping": 15,
                }
            ),
            'end': TimePickerInput(
                options={
                    "format": 'HH:mm',
                    "stepping": 15,
                }
            ),
        }
