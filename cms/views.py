from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Record  # , ActivityType, Activity


def life_logs(request):
    """記録一覧"""
    records = Record.objects.all().order_by('id')
    return render(request, 'cms/logs.html', {'records': records})


def edit_record(request, record_id=None):
    """活動記録の編集"""
    return HttpResponse('活動記録の編集')


def del_record(request, record_id):
    """活動記録の削除"""
    return HttpResponse('活動記録の削除')
