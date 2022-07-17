from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='homepage'),
    path('counter/', views.counter , name='counter'),
    path('objectdb/', views.objectdb , name='objectdb'),


]