from rest_framework import generics, views, viewsets

from apps.api.serializers import ProductOrderSerializer

from apps.api.models import ProductOrder


class ProductOrderListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductOrderSerializer
    queryset = ProductOrder.objects.all()

class ProductOrderDetailView(generics.RetrieveAPIView):
    serializer_class = ProductOrderSerializer
    queryset = ProductOrder.objects.all()

