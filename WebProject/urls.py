from django.contrib import admin
from django.urls import path, include
from PersonalPage import views
urlpatterns = [
    path('home/', include('PersonalPage.urls')),
    path('about/', views.about, name='about'),
    path('github/', views.passion, name='passion'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls)
]
