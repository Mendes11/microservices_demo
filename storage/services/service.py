from django.db import transaction
from django.db.models import F
from django_nameko_standalone import DjangoModels
from nameko.dependency_providers import Config
from nameko.events import EventDispatcher, event_handler


# This is just a template Service and more classes or files could be written.

class StorageService:
    """
    Usage for listening for events:

    @event_handler('dispatching_service_name', 'event_name')
    def some_func_name(self, payload):
        do some business logic here

        # Usage of Django Models:
        # The models enabled are in DJANGO_NAMEKO_STANDALONE_APPS configured
        #in settings.py.
        self.models.ModelName.objects....

        # If you want to dispatch some event:
        self.dispatch('event_name', {content as a dict})

    """
    name = 'storage_service'
    config = Config()
    models = DjangoModels()
    dispatcher = EventDispatcher()

    @event_handler('products', 'product__created')
    def storage_creator(self, payload):
        """Simply create a New Storage for the new product"""
        self.models.Storage.objects.create(product=payload['id'], quantity=0)


    @event_handler('storage', 'storage_operation__requested')
    def storage_manager(self, payload):
        """Updates the current storage status based on the amount in the
        StorageLog"""
        amount = payload['amount']
        product = payload['product']
        storage_operation = self.models.StorageOperation.objects.get(
            id=payload['id'])

        # Acquire a lock in the Model, this is needed due to .update() not
        # calling a post_save signal which is used by the event_sourcing lib.
        try:
            with transaction.atomic():
                storage = self.models.Storage.objects.get(product=product)

                if storage.quantity + amount >= 0:
                    storage.quantity = storage.quantity + amount
                    storage.save()
                    storage_operation.status = 'approved'
                else:
                    storage_operation.status = 'rejected'
        except Exception as e:
            print(str(e))
            storage_operation.status = 'failed'
        storage_operation.save()

    @event_handler('orders', 'product_order__withdraw_requested')
    def create_new_request(self, payload):
        # Here We could just create or do the entire logic.
        self.models.StorageOperation.objects.create(
            product=payload['product'],
            user=payload['user'],
            amount=-payload['amount'],
            order=payload['id'],
        )
