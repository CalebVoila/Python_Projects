# bot_project/urls.py
from django.contrib import admin
from django.urls import path, include
from bot_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('main/', include('bot_app.urls')),
]
