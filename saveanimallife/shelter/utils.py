from .models import *

menu = [{'title': "Animals", 'url_name': 'animals'}, {'title': "About us", 'url_name': 'about_us'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
