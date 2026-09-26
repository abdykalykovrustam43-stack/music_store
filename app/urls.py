from django.urls import path
from django.http import JsonResponse

from .views import (
    SoundListView,
    SoundCreateView,
    SoundUpdateDeleteView,
    RegisterSerializer,
    music_page,
    RegisterListView,
    ProfileListView,
    SavedSoundUpdateDeleteView,
    SavedSoundListCreateView,
)


def home(request):
    return JsonResponse({
        "message": "Music Store API"
    })


urlpatterns = [
    path('', music_page),

    path('sound/', SoundListView.as_view()),

    path('sound/create/', SoundCreateView.as_view()),

    path('sound/<int:pk>/', SoundUpdateDeleteView.as_view()),

    path('register/', RegisterListView.as_view()),

    path('profile/', ProfileListView.as_view()),

    path('saved/', SoundListView.as_view()),
    path('saved/<int:pk>/', SavedSoundUpdateDeleteView.as_view()),
]


