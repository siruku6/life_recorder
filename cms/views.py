from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

from cms.models import Record  # , ActivityType, Activity
from cms.forms import RecordForm


def life_logs(request):
    """活動日一覧"""
    records = Record.objects.all().order_by('id')
    return render(request, 'cms/logs.html', {'records': records})


def edit_record(request, record_id=None):
    """活動日の編集"""
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
    """活動日の削除"""
    # return HttpResponse('活動記録の削除')
    record = get_object_or_404(Record, pk=record_id)
    record.delete()
    return redirect('cms:life_logs')


class Activities(ListView):
    """活動内容の一覧"""
    context_object_name = 'activities'
    template_name = 'cms/activities.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        record = get_object_or_404(Record, pk=kwargs['record_id'])
        activities = record.activities.all().order_by('id')
        self.object_list = activities

        context = self.get_context_data(object_list=self.object_list, record=record)
        return self.render_to_response(context)
