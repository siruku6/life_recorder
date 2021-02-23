from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('logs/', views.life_logs, name='life_logs'),   # 一覧
    path('records/create/', views.edit_record, name='create_record'),  # 登録
    path('records/edit/<int:record_id>/', views.edit_record, name='edit_record'),  # 修正
    path('records/destroy/<int:record_id>/', views.del_record, name='destroy_record'),   # 削除
]
