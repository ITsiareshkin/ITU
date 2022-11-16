from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('user_page/', userpage, name='userpage'),
    path('animals/', animals, name='animals'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
]
