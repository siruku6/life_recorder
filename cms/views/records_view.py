import datetime
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect

from cms.models import Record
from cms.forms import RecordForm


def life_logs(request):
    """活動日一覧"""
    today: datetime = datetime.date.today()

    if not Record.objects.filter(date=today).exists():
        Record(date=today).save()
    records: QuerySet = Record.objects.all().order_by('id')
    return render(request, 'cms/logs.html.haml', {'records': records})


def edit_record(request, record_id=None):
    """活動日の編集"""
    if record_id:
        record: Record = get_object_or_404(Record, pk=record_id)
    else:
        record: Record = Record()

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)

        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('cms:life_logs')
    else:
        form = RecordForm(instance=record)

    return render(request, 'cms/edit_record.html.haml', dict(form=form, record_id=record_id))


def del_record(request, record_id):
    """活動日の削除"""
    # return HttpResponse('活動記録の削除')
    record = get_object_or_404(Record, pk=record_id)
    record.delete()
    return redirect('cms:life_logs')
