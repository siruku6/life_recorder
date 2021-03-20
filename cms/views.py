import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

from cms.models import Record, Activity  # , ActivityType
from cms.forms import RecordForm, ActivityForm


# -----------------------------------------------------------
#                          Record
# -----------------------------------------------------------
def life_logs(request):
    """活動日一覧"""
    records = Record.objects.all().order_by('id')
    return render(request, 'cms/logs.html.haml', {'records': records})


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


# -----------------------------------------------------------
#                         Activity
# -----------------------------------------------------------
class Activities(ListView):
    """活動内容の一覧"""
    context_object_name = 'activities'
    template_name = 'cms/activities.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        record = get_object_or_404(Record, pk=kwargs['record_id'])
        activities = record.activities.all().order_by('id')
        self.object_list = activities

        context = self.get_context_data(
            object_list=self.object_list, record=record
        )

        # import pdb; pdb.set_trace()
        return self.render_to_response(context)


def edit_activity(request, record_id, activity_id=None):
    """活動内容の編集"""
    record = get_object_or_404(Record, pk=record_id)
    if activity_id:
        activity = get_object_or_404(Activity, pk=activity_id)
    else:
        activity = Activity()

    if request.method == 'POST':
        params = preprocess_activity_params(record=record, params=request.POST.copy())
        form = ActivityForm(params, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.record = record
            activity.save()
            return redirect('cms:activities', record_id=record_id)
    else:
        form = ActivityForm(instance=activity)

    return render(
        request, 'cms/edit_activity.html',
        dict(form=form, record_id=record_id, activity_id=activity_id))


def preprocess_activity_params(record, params):
    target_date = record.date.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
    start_hm = params.get('start').split(':')
    end_hm = params.get('end').split(':')

    params['start'] = target_date.replace(hour=int(start_hm[0]), minute=int(start_hm[1]))
    params['end'] = target_date.replace(hour=int(end_hm[0]), minute=int(end_hm[1]))
    return params


def del_activity(request, record_id, activity_id=None):
    """活動内容の削除"""
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    return redirect('cms:activities', record_id=record_id)
