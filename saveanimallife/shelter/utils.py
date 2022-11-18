from django.contrib.auth.mixins import UserPassesTestMixin

from .models import *

menu = [{'title': "Animals", 'url_name': 'animals', 'access': 'all'},
        {'title': "About us", 'url_name': 'about_us', 'access': 'all'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
