from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include('PersonalPage.urls')),
    #path('about/', include('PersonalPage.urls')),
    path('admin/', admin.site.urls),
]
