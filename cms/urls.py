from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 活動日
    path('logs/', views.life_logs, name='life_logs'),
    path('records/create/', views.edit_record, name='create_record'),
    path('records/edit/<int:record_id>/', views.edit_record, name='edit_record'),
    path('records/destroy/<int:record_id>/', views.del_record, name='destroy_record'),

    # 活動内容
    path('records/<int:record_id>/activities/', views.Activities.as_view(), name='activities'),
]
