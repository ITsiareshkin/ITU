from django.contrib.auth.mixins import UserPassesTestMixin

from .models import *
from django.db.models import Q

menu = [{'title': "Animals", 'url_name': 'animals', 'access': 'all'},
        {'title': "About us", 'url_name': 'about_us', 'access': 'all'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

def delete_user(userid):
    try:
        acc = Account.objects.get(pk=userid)
    except:
        return False
    acc.deleted = True
    acc.is_active = False
    if acc.position == 'vet':
        a = Task.objects.filter(vet_id=acc.pk).exclude(status="ended")
        a.update(status="created", task_start=None, task_end=None, vet_id=None)
    elif acc.position == 'verified':
        a = Walk.objects.filter(walker_id=acc.pk).exclude(status="end")
        a.update(status="free", walker_id=None)
    acc.save()
    return True


def unverify_user(userid):
    try:
        acc = Account.objects.get(pk=userid)
    except:
        acc = None
    if acc is not None:
        if acc.position == 'verified':
            acc.position = 'unverified'
            acc.save()
            a = Walk.objects.filter(walker_id=acc.pk).exclude(status="end")
            a.update(status="free", walker_id=None)
        return True


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'