from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=70)
    post = models.TextField(max_length=6000)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
    
    class Meta:
        ordering = ['post_title']

