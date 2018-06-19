from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', null=True, default=1, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    
    def __str__(self):
        return self.title