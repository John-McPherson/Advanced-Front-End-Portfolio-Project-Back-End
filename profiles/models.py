from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-profile_heu292', blank=True
    )
    writer = models.BooleanField(default=False)
    artist = models.BooleanField(default=False)
    letterer = models.BooleanField(default=False)
    editor = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.owner}'s profile"

