from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput  # , DateTimePickerInput
from cms.models import Record, Activity


class RecordForm(forms.ModelForm):
    """活動日のフォーム"""
    class Meta:
        model = Record
        fields = ('date', 'comment', )
        widgets = {
            # 'date': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),

            'date': DatePickerInput(
                options={
                    'format': '%Y-%m-%d',
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
        }


class ActivityForm(forms.ModelForm):
    """活動内容のフォーム"""
    # TODO: activity_type は、選択式のみでなく、入力も可能にする
    #   https://stackoverflow.com/questions/24783275/django-form-with-choices-but-also-with-freetext-option
    #   https://teratail.com/questions/201160
    #   https://blog.qux-jp.com/2018/04/169
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    class Meta():
        model = Activity
        fields = ('activity_type', 'name', 'start', 'end', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'start': forms.TextInput(attrs={'class': 'form-control'}),
            # 'end': forms.TextInput(attrs={
            #     'class': 'form-control datetimepicker',
            #     'id': 'datetimepicker1',
            # }),
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
