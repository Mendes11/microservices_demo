from rest_framework import serializers

from apps.api.models import Storage, StorageOperation


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class StorageOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageOperation
        fields = '__all__'
