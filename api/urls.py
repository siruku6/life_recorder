from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('records', views.RecordViewSet)

app_name = 'api/v1'
urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/records', views.records, name='records')
]
