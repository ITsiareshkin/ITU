from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import *
from django.views.generic.list import BaseListView
# from django.views.generic.edit import BaseCreateView
from django.views.generic.base import TemplateResponseMixin
import sys

from .forms import *
from .utils import *
from .models import *

menu = [{'title': "Animals", 'url_name': 'animals'},
        {'title': "About us", 'url_name': 'about_us'}]

class ShelterHome(DataMixin, TemplateView):
    template_name = 'shelter/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home page")
        return dict(list(context.items()) + list(c_def.items()))

class AnimalList(DataMixin, BaseListView, TemplateResponseMixin):
    model = Animal
    template_name = 'shelter/animal.html'
    context_object_name = 'animal'

    def get(self, request, *args, **kwargs):
        f_kind = request.GET.get('kind', '')
        f_gender = request.GET.get('gender', '')
        f_age = request.GET.get('age', '')
        self.object_list = Animal.objects.all()

        if f_kind != '':
            if f_kind == 'cat':
                self.object_list = self.object_list.filter(kind='Cat')
            elif f_kind == 'dog':
                self.object_list = self.object_list.filter(kind='Dog')

        if f_gender != '':
            if f_gender == 'female':
                self.object_list = self.object_list.filter(gender='Female')
            elif f_gender == 'male':
                self.object_list = self.object_list.filter(gender='Male')

        if f_age != '':
            if f_age == 'baby':
                self.object_list = self.object_list.filter(age__lte='1')
            elif f_age == 'teen':
                self.object_list = self.object_list.filter(age__gt='1', age__lt='5')
            elif f_age == 'adult':
                self.object_list = self.object_list.filter(age__gte='5')


        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
    #
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Animals"
        context['menu'] = menu
        return context

@method_decorator(login_required, name='dispatch')
class AnimalProfile(DataMixin, DetailView):
    model = Animal
    template_name = 'shelter/animal_profile.html'
    pk_url_kwarg = 'animalid' # make slug
    context_object_name = 'animal'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['animal']
        context['menu'] = menu
        return context

@method_decorator(login_required, name='dispatch')
class EditAnimal(DataMixin, UserPassesTestMixin, UpdateView):
    model = Animal
    template_name = 'shelter/edit_animal_profile.html'
    form_class = EditAnimalForm
    pk_url_kwarg = 'animalid'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Animal profile")
        return dict(list(context.items()) + list(c_def.items()))

    def test_func(self):
        if self.request.user.position == "employee":
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('animals')


class ShowAddAnimal(DataMixin, UserPassesTestMixin, CreateView):
    paginate_by = 5 # wtf
    form_class = AddAnimalForm
    template_name = 'shelter/addanimal.html'
    success_url = reverse_lazy('animals')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add animal")
        return dict(list(context.items()) + list(c_def.items()))


def about_us(request):
    context = {
        'menu': menu,
        'title': 'About Us'
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


@method_decorator(login_required, name='dispatch')
class Mypage(DataMixin, TemplateView):
    template_name = 'shelter/mypage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="My profile")
        return dict(list(context.items()) + list(c_def.items()))


@method_decorator(login_required, name='dispatch')
class PasswordChange(DataMixin, PasswordChangeView):
    template_name = 'shelter/change_password.html'
    form_class = ChangePasswdForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="My profile")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('mypage')


@method_decorator(login_required, name='dispatch')
class EditProfile(DataMixin, generic.UpdateView):
    model = Account
    template_name = 'shelter/edit_profile.html'
    form_class = EditProfileForm

    def get_object(self):
        return self.request.user

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="My profile")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('mypage')


@method_decorator(login_required, name='dispatch')
class ShowUserPage(UserPassesTestMixin, DetailView):
    model = Account
    template_name = 'shelter/userpage.html'
    context_object_name = 'account'
    pk_url_kwarg = 'userid'

    def test_func(self):
        if self.request.user.position == "employee" or self.request.user.position == "admin":
            return True
        return False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "User page"
        context['menu'] = menu
        return context


@method_decorator(login_required, name='dispatch')
class ShowUsers(UserPassesTestMixin, ListView):
    paginate_by = 5
    model = Account
    template_name = 'shelter/users.html'
    context_object_name = 'accounts'
    pk_url_kwarg = 'userid'

    def test_func(self):
        if self.request.user.position == "employee" or self.request.user.position == "admin":
            return True
        return False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "User page"
        context['menu'] = menu
        return context


@method_decorator(login_required, name='dispatch')
class UserEdit(DataMixin, UserPassesTestMixin, generic.UpdateView):
    model = Account
    template_name = 'shelter/edit_profile.html'
    form_class = EditUserForm
    pk_url_kwarg = 'userid'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="My profile")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('mypage')

    def test_func(self):
        if self.request.user.position == "admin":
            return True
        return False


def plug(request):
    context = {
        'menu': menu,
        'title': 'About Us'
    }
    if request.user.position == "employee":
        print("idiot&")
    return render(request, 'shelter/index.html', context=context)
