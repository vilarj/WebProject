from django.contrib import admin
from django.urls import path, include
from PersonalPage import views

urlpatterns = [
    path('home/', include('PersonalPage.urls')),
    path('about/', views.about),
    path('passion/', views.passion),
    path('admin/', admin.site.urls),
]
