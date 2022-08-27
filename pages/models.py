from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from project.models import Project



class Page(models.Model):
    '''
    Page model. Linked to project 
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_owner')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    cover = models.BooleanField(default=False)
    roughs = models.ImageField(
        upload_to='images/', default='../default-page_xo6mbk', blank=True
    )
    inks = models.ImageField(
        upload_to='images/', default='../default-page_xo6mbk', blank=True
    )
    colors = models.ImageField(
        upload_to='images/', default='../default-page_xo6mbk', blank=True
    )
    letters = models.ImageField(
        upload_to='images/', default='../default-page_xo6mbk', blank=True
    )

    
    # writers = models.ManyToManyField(Profile, related_name='writers', related_query_name='writers',blank=True)
    # artists = models.ManyToManyField(Profile, related_name='artists', related_query_name='artists',blank=True)
    # letterers = models.ManyToManyField(Profile, related_name='letterers', related_query_name= 'letterers', blank=True)
    # editors = models.ManyToManyField(Profile, related_name='editors', related_query_name='editors', blank=True)
    # pages = models.IntegerField(default=22)
    
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.title

