from django.shortcuts import render
from rest_framework import generics
from rest_framework .permissions import AllowAny, IsAuthenticated

from .models import Sound, SavedSound
from .serializers import (SoundListSerializer, RegisterSerializer, SavedSoundSerializer )

class SoundListView(generics.ListAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundListSerializer





class SoundCreateView(generics.CreateAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundListSerializer


class SoundUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundListSerializer


class RegisterListView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProfileListView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return self.request.user


class SavedSoundListCreateView(generics.ListCreateAPIView):
    serializer_class = SavedSoundSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SavedSound.objects.filter(
            user=self.request.user
        )


    def perform_create(self , serializer):
        serializer.save(user=self.request.user)


class SavedSoundUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SavedSoundSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SavedSound.objects.filter(
            user=self.request.user
        )

def music_page(request):
    return render(request, 'music.html')





