from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='homepage'),
    path('counter/', views.counter , name='counter'),
    path('objectdb/', views.objectdb , name='objectdb'),
    path('register/', views.register , name='register'),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
    path('post/<int:pk>/', views.post , name='post'),
    path('search/', views.search , name='search'),
    path('<str:room>/', views.room , name='room'),
    path('checkview', views.checkview , name='checkview'),
    path('testapi/', views.TestAPI.as_view() , name='getAPI'),
]

