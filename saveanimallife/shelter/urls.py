from django.urls import path
from .views import *

urlpatterns = [
    path('', ShelterHome.as_view(), name='home'),
    path('mypage/', UserProfileWalks.as_view(), name='mypage'),

    path('animals/', Animals_Ajax.as_view(), name='animals'),
    path('animals/<int:animalid>/', AnimalProfile.as_view(), name='animal'),
    path('addanimal/', ShowAddAnimal.as_view(), name='addanimal'),

    path('animals/<int:animalid>/edit/', EditAnimal.as_view(), name='edit_animal'),
    path('animals/<int:animalid>/delete/', AnimalDelete.as_view(), name='animal_delete'),
    path('animals/<int:animalid>/favorite/', favorites, name='favorites'),

    path('about_us/', about_us, name='about_us'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('edit_profile/', EditProfile.as_view(), name='edit_profile'),
    path('change_password/', PasswordChange.as_view(), name='change_password'),
    path('user/<username>/', ShowUserPage.as_view(), name='show_user'),
    path('user/edit/<username>/', UserEdit.as_view(), name='user_edit'),
    path('users/', ShowUsers.as_view(), name='users'),
    path('users/adduser/', AddUser.as_view(), name='adduser'),

    path('manage_walks/<int:animalid>/', ManageAnimalWalks.as_view(), name="manage_walks"),
    path('user_walks/<int:animalid>/', UserWalks.as_view(), name="user_walks"),
    path('today_walks/', TodayWalks.as_view(), name="today_walks"),

    path('accounts/login/', Login.as_view(), name='login_logout'),
]