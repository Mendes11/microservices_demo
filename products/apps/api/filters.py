from django_filters import rest_framework as filters

from apps.api.models import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ('product_type', 'name')
