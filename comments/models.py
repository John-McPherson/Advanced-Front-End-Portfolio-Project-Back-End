from django.db import models
from django.contrib.auth.models import User
from pages.models import Page


class Comment(models.Model):
    """
    Comment model, related to User and Page
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
