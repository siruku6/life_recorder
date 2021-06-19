from django.urls import path
from cms.views import home_view, records_view, activity_types_view, activities_view

app_name = 'cms'
urlpatterns = [
    path('', home_view.index, name='index'),

    # 活動日
    path('logs/', records_view.life_logs, name='life_logs'),
    path('records/create/', records_view.edit_record, name='create_record'),
    path('records/<int:record_id>/edit/', records_view.edit_record, name='edit_record'),
    path('records/<int:record_id>/destroy/', records_view.del_record, name='destroy_record'),

    # 活動種別
    path('activity_types/', activity_types_view.activity_types, name='activity_types'),
    path('activity_types/new/', activity_types_view.new, name='new_activity_type'),
    path('activity_types/create/', activity_types_view.create_or_update, name='create_or_update_activity_type'),
    # path('activity_types/<int:activity_type_id>/edit/', activity_types_view.edit, name='edit_activity_type'),
    path('activity_types/<int:activity_type_id>/destroy/', activity_types_view.delete, name='destroy_activity_type'),

    # 活動内容
    path('records/<int:record_id>/activities/', activities_view.Activities.as_view(), name='activities'),
    path('records/<int:record_id>/activities/create/', activities_view.edit, name='create_activity'),
    path('records/<int:record_id>/activities/<int:activity_id>/edit/', activities_view.edit, name='edit_activity'),
    path(
        'records/<int:record_id>/activities/<int:activity_id>/destroy/',
        activities_view.delete, name='destroy_activity'
    ),
]
