from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hospitals-list/', views.hospitals_list, name='hospitals-list'),
]