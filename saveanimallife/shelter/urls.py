from django.urls import path
from .views import *

urlpatterns = [
    path('', ShelterHome.as_view(), name='home'),
    path('mypage/', Mypage.as_view(), name='mypage'),
    path('animals/', animals, name='animals'),
    path('about_us/', about_us, name='about_us'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('edit_profile/', EditProfile.as_view(), name='edit_profile'),
    path('change_password/', PasswordChange.as_view(), name='change_password')
]
