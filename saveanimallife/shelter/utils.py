from .models import *

menu = [{'title': "Animals", 'url_name': 'animals'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
