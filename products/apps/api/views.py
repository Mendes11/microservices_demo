from rest_framework import generics, views, viewsets

from apps.api.filters import ProductFilter
from apps.api.models import ProductType, Product
from apps.api.serializers import ProductTypeSerializer, \
    ProductSerializer


class ProductTypeListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

