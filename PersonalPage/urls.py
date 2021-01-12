from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/about/', views.about, name='about'),
    # path('home/passion/', views.about, name='passion'),
    # path('', views.about, name='about'),
]