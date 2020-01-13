import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Storage(models.Model):
    """Current State of the Storage Updated by internal Services"""
    product = models.UUIDField(unique=True)
    quantity = models.IntegerField()


class StorageOperation(models.Model):
    """Operations made in the Storage."""
    STATUS_OPTIONS = (('requested', 'Requested'),
                      ('approved', 'Approved'),
                      ('rejected', 'Rejected'),
                      ('failed', 'Failed'))

    user = models.UUIDField()
    product = models.UUIDField()
    amount = models.IntegerField()
    # Used by the system
    order = models.UUIDField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS,
                              default='requested')
