from django.db import models
from django.contrib.auth.models import User


class Sound(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class SavedSound(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='saved_sounds' )
    sound = models.ForeignKey(Sound,on_delete=models.CASCADE, related_name='saved_by'
)

created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('user', 'sound')

    def __str__(self):
        return f'{self.user.username} - {self.sound.title}'










