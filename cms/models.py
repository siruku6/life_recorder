import datetime
from django.db import models
from django.utils import timezone


class Record(models.Model):
    """Record"""
    date = models.DateField(
        '日付', max_length=255,
        default=datetime.date.today,
        unique=True,
        null=False
    )
    comment = models.TextField('コメント', blank=True, null=True)
    # page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return 'id({}) {}'.format(self.id, self.date.isoformat())


class ActivityType(models.Model):
    """ActivityType"""
    name = models.CharField('種別', max_length=50, null=False, unique=True)
    color = models.CharField('色コード', max_length=20, blank=True, null=True)

    def __str__(self):
        return 'id:({}) {}'.format(self.id, self.name)


class Activity(models.Model):
    """Activity"""
    record = models.ForeignKey(Record, verbose_name='活動日', related_name='activities', on_delete=models.CASCADE)
    activity_type = models.ForeignKey(
        ActivityType, verbose_name='種別', related_name='activities', on_delete=models.SET_NULL, null=True
    )
    name = models.CharField('内容', max_length=255, null=False)
    start = models.DateTimeField('開始', default=timezone.now, null=False)
    end = models.DateTimeField('終了', default=timezone.now, null=False)
    spent_time = models.PositiveIntegerField('消費時間', null=False)  # seconds

    def __str__(self):
        act_type = self.activity_type
        display = 'id({}) {} - {}'.format(self.id, self.activity_type.name, self.name) \
            if act_type is not None else self.name
        return display


class TemplateActivity(models.Model):
    """TemplateActivity"""
    activity_type = models.ForeignKey(
        ActivityType, verbose_name='種別', related_name='template_activities',
        on_delete=models.CASCADE, null=True
    )
    name = models.CharField('内容', max_length=255, null=False, unique=True)

    def __str__(self):
        act_type = self.activity_type
        display = 'id({}) {} - {}'.format(self.id, self.activity_type.name, self.name) \
            if act_type is not None else self.name
        return display


DEFAULT_ACTIVITY_TYPES = [
    {"name": "Study", "color": "#08f718"},
    {"name": "Sports", "color": "#004cff"},
    {"name": "Necessity", "color": "#00d9ff"},
    {"name": "Challenge", "color": "#fff700"},
    {"name": "Relaxation", "color": "#ffb3e7"}
]


def seed_default_data(sender, **kwargs):
    default_types = [default_type['name'] for default_type in DEFAULT_ACTIVITY_TYPES]
    existing_types = ActivityType.objects \
                                 .filter(name__in=default_types) \
                                 .values_list('name', flat=True)
    lacking_types = set(default_types) - set(existing_types)

    for type_dict in DEFAULT_ACTIVITY_TYPES:
        if type_dict['name'] in lacking_types:
            ActivityType.objects.create(**type_dict)
