from django.urls import path
from .views import *

urlpatterns = [
    path('', ShelterHome.as_view(), name='home'),
    path('mypage/', userpage, name='userpage'),
    path('animals/', animals, name='animals'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name='register')
]
