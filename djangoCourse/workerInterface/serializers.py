from rest_framework import serializers
from .models import Worker, BasicInfo, ContactInfo, EmerContactInfo

class WorkerSerializer(serializers.ModelSerializer):
    class meta:
        model = Worker
        fields = '__all__'


class BasicInfo(serializers.ModelSerializer):
    workerId = Worker
    class meta:
        model = BasicInfo
        fields = ['workerId', 'dateOfBirth', 'gender', 'marialStatus',
                  'nationality', 'ethnic', 'bankAccount']

