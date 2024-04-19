# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voice_assistant/', views.voice_assistant, name='voice_assistant'),
]
