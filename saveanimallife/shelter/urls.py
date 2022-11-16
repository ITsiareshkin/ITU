from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('user_page', userpage, name='userpage'),
    path('about_us', about_us, name='about_us'),
    path('animals', animals, name='about_us'),
    path('donate', donate, name='log_in'),
]
