from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),

    path('', views.home, name='home'),
    path('sched/', views.Schedgames, name='Schedgames'),
    path('profile/', views.PlayerProf, name='PlayerProf'),

    path('matchups/<str:pk_tests>/', views.matchups, name='matchups'),

    path('matchups/', views.matchups, name='matchups'),

    path('matchups/<str:pk_tests>/', views.matchups, name='matchups'),

    path('create_booking/', views.createbooking, name='create_booking'),
    path('update_booking/<str:pk>', views.updatebooking, name='update_booking'),
    path('delete_booking/<str:pk>', views.deletebooking, name='delete_booking'),
]