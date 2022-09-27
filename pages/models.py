from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from project.models import Project


class Page(models.Model):
    """
    Page model. Linked to project
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="page_owner")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    page_number = models.IntegerField()
    cover = models.BooleanField(default=False)
    roughs = models.ImageField(
        upload_to="images/", default="../default-page_xo6mbk", blank=True
    )
    inks = models.ImageField(
        upload_to="images/", default="../default-page_xo6mbk", blank=True
    )
    colors = models.ImageField(
        upload_to="images/", default="../default-page_xo6mbk", blank=True
    )
    letters = models.ImageField(
        upload_to="images/", default="../default-page_xo6mbk", blank=True
    )

    class Meta:
        ordering = ["page_number"]

    def __str__(self):
        return self.title
