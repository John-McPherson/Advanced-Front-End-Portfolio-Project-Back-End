from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from profiles.models import Profile


class Project(models.Model):
    """
    Project model. Linked to user profile
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, unique=True)
    color = models.BooleanField(default=False)
    writers = models.ManyToManyField(
        Profile, related_name="writers", related_query_name="writers", blank=True
    )
    artists = models.ManyToManyField(
        Profile, related_name="artists", related_query_name="artists", blank=True
    )
    letterers = models.ManyToManyField(
        Profile, related_name="letterers", related_query_name="letterers", blank=True
    )
    editors = models.ManyToManyField(
        Profile, related_name="editors", related_query_name="editors", blank=True
    )
    colorists = models.ManyToManyField(
        Profile, related_name="colorists", related_query_name="colorists", blank=True
    )
    pages = models.IntegerField(default=22)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
