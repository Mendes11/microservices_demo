from rest_framework import generics

from apps.api.models import Storage, StorageOperation
from apps.api.serializers import StorageSerializer, StorageOperationSerializer


class StorageListView(generics.ListAPIView):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()


class StorageDetailView(generics.RetrieveAPIView):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()


class StorageOperationListCreateView(generics.ListCreateAPIView):
    serializer_class = StorageOperationSerializer
    queryset = StorageOperation.objects.all()


class StorageOperationDetailView(generics.RetrieveAPIView):
    serializer_class = StorageOperationSerializer
    queryset = StorageOperation.objects.all()
