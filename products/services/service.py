from django_nameko_standalone import DjangoModels
from nameko.dependency_providers import Config
from nameko.events import EventDispatcher, event_handler


# This is just a template Service and more classes or files could be written.

class MyService:
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
    name = 'service_name'
    config = Config()
    models = DjangoModels()
    dispatcher = EventDispatcher()


