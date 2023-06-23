from django.urls import path
from . import views #from present working directory import views
urlpatterns = [
    path('', views.home, name='home-page'),  #path to the home page of the app
    path('register/', views.register, name='register'),  #path to the register page of the app
    path('login/', views.loginpage, name='login'),  #path to the login page of the app
    path('logout/', views.LogoutView, name='logout'),  #path to the logout page of the app
    path('delete-task/<str:name>/', views.DeleteTask, name='delete'), #path to the delete task page of the app
    path('update/<str:name>/', views.Update, name='update'),  #path to the update page of the app
]