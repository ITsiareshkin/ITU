from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from .forms import RegisterUserForm
from .utils import *

menu = [{'title': "Animals", 'url_name': 'animals'}]


class ShelterHome(DataMixin, TemplateView):
    template_name = 'shelter/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home page")
        return dict(list(context.items()) + list(c_def.items()))


def animals(request):
    context = {
        'menu': menu,
        'title': 'Animals'
    }
    return render(request, 'shelter/index.html', context=context)


class Register(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shelter/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))


class Login(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'shelter/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Log in")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')



def userpage(request):
    context = {
        'menu': menu,
        'title': 'User page'
    }
    return render(request, 'shelter/index.html', context=context)
