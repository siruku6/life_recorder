from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    path('', views.index, name='index'),

    # 活動日
    path('logs/', views.life_logs, name='life_logs'),
    path('records/create/', views.edit_record, name='create_record'),
    path('records/<int:record_id>/edit/', views.edit_record, name='edit_record'),
    path('records/<int:record_id>/destroy/', views.del_record, name='destroy_record'),

    # 活動種別
    path('activity_types/', views.activity_types, name='activity_types'),
    path('activity_types/new/', views.new_activity_type, name='new_activity_type'),
    path('activity_types/create/', views.create_or_update_activity_type, name='create_or_update_activity_type'),
    # path('activity_types/<int:activity_type_id>/edit/', views.edit_activity_type, name='edit_activity_type'),
    path('activity_types/<int:activity_type_id>/destroy/', views.del_activity_type, name='destroy_activity_type'),

    # 活動内容
    path('records/<int:record_id>/activities/', views.Activities.as_view(), name='activities'),
    path('records/<int:record_id>/activities/create/', views.edit_activity, name='create_activity'),
    path('records/<int:record_id>/activities/<int:activity_id>/edit/', views.edit_activity, name='edit_activity'),
    path('records/<int:record_id>/activities/<int:activity_id>/destroy/', views.del_activity, name='destroy_activity'),
]
