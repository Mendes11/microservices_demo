from rest_framework import serializers

from apps.api.models import ProductOrder


class ProductOrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)

    class Meta:
        model = ProductOrder
        fields = '__all__'
