from django.db.models import AutoField
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class OldPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = oldperson_info
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    oldperson = PrimaryKeyRelatedField(many=False, queryset=oldperson_info.objects.all())
    # oldperson_username = serializers.CharField(source='web_oldperson_info.username')

    class Meta:
        model = event_info
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_info
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = volunteer_info
        fields = '__all__'


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = sys_user
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
