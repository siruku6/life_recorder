from django.db.models import Sum
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, CustomSerializer

from django.contrib.auth.models import User, Group
from cms.models import Activity


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RecordViewSet(viewsets.ModelViewSet):
    # queryset = Record.objects.all()
    queryset = Activity.objects.prefetch_related() \
                               .values('record__date', 'activity_type__name') \
                               .annotate(sum_time=Sum('spent_time')) \
                               .order_by('record__date', 'activity_type__name')

    # serializer_class = RecordSerializer
    serializer_class = CustomSerializer
    permission_classes = [permissions.IsAuthenticated]
