from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput  # , DateTimePickerInput
from cms.models import Record, Activity


class RecordForm(forms.ModelForm):
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


class ActivityTypeForm(forms.Form):
    """活動内容のフォーム"""
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(),
    )
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )
    color = forms.CharField(
        max_length=7,
        widget=forms.TextInput(
            attrs={'type': 'color', 'class': 'form-control'}
        ),
    )

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color.startswith('#'):
            raise forms.ValidationError("半角の # で始まる文字列を入力してして下さい")
        return color


class ActivityForm(forms.ModelForm):
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

    # INFO: 日付系のsample
    # purchased_date = forms.DateTimeField(
    #     label='購入日',
    #     required=True,
    #     widget=forms.DateInput(attrs={"type": "date"}),
    #     input_formats=['%Y-%m-%d']
    # )

    # 日付だけでなく、日時にする場合は以下
    # datetime = forms.DateTimeField(
    #    label='日時',
    #    required=True,
    #    widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    #    input_formats=['%Y-%m-%dT%H:%M']
    # )
