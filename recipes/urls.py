from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="recipes-landing"),
    path('home/', views.home, name="recipes-home"),
    path('about/', views.about, name="recipes-about"),
]