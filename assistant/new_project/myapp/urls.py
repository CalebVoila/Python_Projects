# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voice_assistant/', views.voice_assistant, name='voice_assistant'),
    path('play/', views.after_joke, name='joke'),
    path('news/', views.news, name='news'),
    path('sports/', views.sports, name='sports'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('cartoon/', views.cartoon, name='cartoon'),
]
