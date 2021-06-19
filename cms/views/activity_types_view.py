from django.shortcuts import render, get_object_or_404, redirect

from cms.models import ActivityType
from cms.forms import ActivityTypeForm


# -----------------------------------------------------------
#                      Activity Type
# -----------------------------------------------------------
def activity_types(request):
    """活動種別一覧"""
    types = ActivityType.objects.all().order_by('id')
    return render(request, 'cms/activity_types.html.haml', {'activity_types': types})


def new(request):
    """活動種別登録画面"""
    form = ActivityTypeForm(request.GET)
    return render(request, 'cms/edit_activity_type.html.haml', {'form': form},)


# def edit_activity_type(request, activity_type_id=None):
#     """活動種別登録画面"""
#     activity_type: ActivityType = get_object_or_404(ActivityType, pk=activity_type_id)
#     # INFO: forms.Form には instance という引数がなく、代わりに initial をとる
#     form = ActivityTypeForm(initial=activity_type)

#     return render(
#         request,
#         'cms/edit_activity_type.html.haml',
#         dict(form=form, activity_type_id=activity_type_id),
#     )


def create_or_update(request, activity_type_id=None):
    form = ActivityTypeForm(request.POST)
    is_valid = form.is_valid()

    if is_valid:
        activity_type = ActivityType(**form.cleaned_data)
        if activity_type_id:
            activity_type = get_object_or_404(activity_type, pk=activity_type_id)

        activity_type.save()
        return redirect('cms:activity_types')
    else:
        return render(
            request,
            'cms/edit_activity_type.html.haml',
            dict(form=form, activity_type_id=activity_type_id)
        )


def delete(_, activity_type_id):
    """活動日の削除"""
    activity_type = get_object_or_404(ActivityType, pk=activity_type_id)
    activity_type.delete()
    return redirect('cms:activity_types')
