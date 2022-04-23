from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=70)
    post = models.TextField(max_length=6000)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.post_title
    
    class Meta:
        ordering = ['post_title']

