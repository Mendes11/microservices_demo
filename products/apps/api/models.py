import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductType(BaseModel):
    name = models.CharField(max_length=200)


class Product(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
