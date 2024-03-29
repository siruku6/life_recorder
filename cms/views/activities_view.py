import datetime
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

from cms.models import Record, Activity, TemplateActivity
from cms.forms import ActivityForm


# -----------------------------------------------------------
#                         Activity
# -----------------------------------------------------------
class Activities(ListView):
    """活動内容の一覧"""
    context_object_name = 'activities'
    template_name = 'cms/activities.html.haml'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        record = get_object_or_404(Record, pk=kwargs['record_id'])
        activities = record.activities.select_related('activity_type').all().order_by('id')
        self.object_list = activities

        context = self.get_context_data(
            object_list=self.object_list, record=record
        )

        return self.render_to_response(context)


def edit(request, record_id, activity_id=None):
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
            create_template_activity(params)

            return redirect('cms:activities', record_id=record_id)
    else:
        form = ActivityForm(instance=activity)

    template_activities: QuerySet = TemplateActivity.objects \
                                                    .all() \
                                                    .order_by('name')

    return render(
        request, 'cms/edit_activity.html.haml',
        dict(
            form=form, record_id=record_id, activity_id=activity_id,
            template_activities=template_activities
        )
    )


def preprocess_activity_params(record, params):
    target_date = datetime.datetime.combine(
        record.date,
        datetime.time(),
        tzinfo=datetime.timezone(datetime.timedelta(hours=9))
    )
    start_hm = params.get('start').split(':')
    end_hm = params.get('end').split(':')
    start_dt = target_date.replace(hour=int(start_hm[0]), minute=int(start_hm[1]))
    end_dt = target_date.replace(hour=int(end_hm[0]), minute=int(end_hm[1]))

    params['start'] = start_dt
    params['end'] = end_dt
    params['spent_time'] = (end_dt - start_dt).seconds
    return params


def create_template_activity(params: dict) -> TemplateActivity:
    tmp_act, _ = TemplateActivity.objects.update_or_create(
        name=params['name'], defaults={'activity_type_id': params['activity_type']}
    )
    return tmp_act


def delete(request, record_id: int, activity_id: int = None):
    """活動内容の削除"""
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    return redirect('cms:activities', record_id=record_id)
