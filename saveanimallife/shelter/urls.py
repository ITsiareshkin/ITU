from django.urls import path
from .views import *

urlpatterns = [
    path('', ShelterHome.as_view(), name='home'),
    path('mypage/', UserProfileWalks.as_view(), name='mypage'),

    path('animals/', AnimalList.as_view(), name='animals'),
    path('animals/<int:animalid>/', AnimalProfile.as_view(), name='animal'),
    path('animals/addanimal', ShowAddAnimal.as_view(), name='addanimal'),
    path('animals/edit/<int:animalid>', EditAnimal.as_view(), name='edit_animal'),

    path('about_us/', about_us, name='about_us'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('edit_profile/', EditProfile.as_view(), name='edit_profile'),
    path('change_password/', PasswordChange.as_view(), name='change_password'),
    path('user/<username>/', ShowUserPage.as_view(), name='show_user'),
    path('user/edit/<username>', UserEdit.as_view(), name='user_edit'),
    path('users/', ShowUsers.as_view(), name='users'),
    path('users/adduser/', AddUser.as_view(), name='adduser'),

    path('manage_walks/<int:animalid>/', ManageAnimalWalks.as_view(), name="manage_walks"),
    path('user_walks/<int:animalid>/', UserWalks.as_view(), name="user_walks"),
    path('today_walks/', TodayWalks.as_view(), name="today_walks"),

    path('manage_tasks/<int:animalid>/', ManageTasksForVet.as_view(), name="manage_tasks"),
    path('task/<int:taskid>/', ShowTask.as_view(), name="task"),
    path('new_tasks/', NewTasks.as_view(), name="new_tasks"),
    path('my_tasks/', MyTasks.as_view(), name="my_tasks"),
]