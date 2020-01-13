from django_nameko_standalone import DjangoModels
from nameko.dependency_providers import Config
from nameko.events import EventDispatcher, event_handler


# This is just a template Service and more classes or files could be written.

class PaymentService:
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
    name = 'payment'
    config = Config()
    models = DjangoModels()
    dispatch = EventDispatcher()

    @event_handler('orders', 'product_order__payment_validation_requested')
    def handle_payment(self, payload):
        # The API should dispatch the payment, but since I'm bypassing it...
        self.dispatch('order_payment_confirmed', {'order': payload['id'],
                                                  'value': 10})


class OrderManager:
    name = 'order_manager'
    config = Config()
    models = DjangoModels()
    dispatch = EventDispatcher()

    @event_handler('orders', 'product_order__requested')
    def request_payment(self, payload):
        # Do Something for validation here.
        order = self.models.ProductOrder.objects.get(id=payload['id'])
        order.status = 'payment_validation_requested'
        order.save()

    @event_handler('payment', 'order_payment_confirmed')
    def request_storage_approval(self, payload):
        order = payload['order']
        order = self.models.ProductOrder.objects.get(id=order)
        order.status = 'withdraw_requested'
        order.save()

    @event_handler('storage', 'storage_operation__failed')
    def handle_failed_withdraw(self, payload):
        order = payload['order']
        order = self.models.ProductOrder.objects.get(id=order)
        order.status = 'failed'
        order.save()

    @event_handler('storage', 'storage_operation__rejected')
    def handle_rejected_withdraw(self, payload):
        order = payload['order']
        order = self.models.ProductOrder.objects.get(id=order)
        order.status = 'failed'
        order.save()

    @event_handler('storage', 'storage_operation__approved')
    def request_delivery(self, payload):
        order = payload['order']
        order = self.models.ProductOrder.objects.get(id=order)
        order.status = 'delivery_requested'
        order.save()
