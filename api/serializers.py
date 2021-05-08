from django.contrib.auth.models import User, Group
# from cms.models import Record, Activity, ActivityType
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class ActivityTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ActivityType
#         fields = ['id', 'name']


# class ActivitySerializer(serializers.ModelSerializer):
#     activity_type = ActivityTypeSerializer(read_only=True)

#     class Meta:
#         model = Activity
#         fields = ['id', 'activity_type', 'name', 'start', 'spent_time']


# class RecordSerializer(serializers.ModelSerializer):
#     activities = ActivitySerializer(many=True, read_only=True)
#     # activities = serializers.PrimaryKeyRelatedField(many=True, queryset=Activity.objects.all())

#     class Meta:
#         model = Record
#         fields = ['id', 'date', 'comment', 'activities']


class CustomSerializer(serializers.Serializer):
    # TODO: Datetime ではなく、 Date のfieldにする
    record__date = serializers.DateTimeField()
    activity_type__name = serializers.CharField(max_length=100)
    sum_time = serializers.IntegerField()
