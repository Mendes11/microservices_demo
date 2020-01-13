import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





class ProductOrder(BaseModel):
    STATUS_CHOICES = (('requested', 'Requested'),
                      ('payment_validation_requested', 'Pending Payment'),
                      ('withdraw_requested', 'Withdraw Requested'),
                      ('request_rejected', 'Order Rejected'),
                      ('delivery_requested', 'Delivery Requested'),
                      ('failed', 'Order Failed'))

    product = models.UUIDField()
    user = models.UUIDField()
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES,
                              default='requested')
