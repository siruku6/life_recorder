import datetime
from django.db import models
from django.utils import timezone


class Record(models.Model):
    """Record"""
    date = models.DateTimeField(
        '日付', max_length=255,
        default=datetime.datetime.today,
        null=False
    )
    comment = models.TextField('コメント', blank=True, null=True)
    # page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.date.isoformat()


class ActivityType(models.Model):
    """ActivityType"""
    name = models.CharField('種別', max_length=50, null=False)
    color = models.CharField('色コード', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activity"""
    record = models.ForeignKey(Record, verbose_name='活動日', related_name='activities', on_delete=models.CASCADE)
    activity_type = models.ForeignKey(ActivityType, verbose_name='種別', related_name='activities', on_delete=models.SET_NULL, null=True)
    name = models.CharField('内容', max_length=255, null=False)
    start = models.DateTimeField('開始', default=timezone.now, null=False)
    end = models.DateTimeField('終了', default=timezone.now, null=False)

    def __str__(self):
        act_type = self.activity_type
        display = '{}: {}'.format(self.activity_type.name, self.name) if act_type is not None else self.name
        return display