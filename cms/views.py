from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import Record  # , ActivityType, Activity
from cms.forms import RecordForm


def life_logs(request):
    """記録一覧"""
    records = Record.objects.all().order_by('id')
    return render(request, 'cms/logs.html', {'records': records})


def edit_record(request, record_id=None):
    """活動記録の編集"""
    if record_id:
        record = get_object_or_404(Record, pk=record_id)
    else:
        record = Record()

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('cms:life_logs')
    else:
        form = RecordForm(instance=record)

    return render(request, 'cms/edit_record.html', dict(form=form, record_id=record_id))


def del_record(request, record_id):
    """活動記録の削除"""
    return HttpResponse('活動記録の削除')
