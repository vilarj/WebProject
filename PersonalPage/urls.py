from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.about, name='about'),
    path('home/', views.passion, name='passion'),
]