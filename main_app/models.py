from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

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

HOBBY_CATEGORY_CHOICES = [
    ('Arts & Crafts', 'Arts & Crafts'),
    ('Collecting', 'Collecting'),
    ('Foodie', 'Foodie'),
    ('Games', 'Games'),
    ('Lucrative', 'Lucrative'),
    ('Music', 'Music'),
    ('Outdoors', 'Outdoors'),
    ('Performing Arts', 'Performing Arts'),
    ('Pets', 'Pets'),
    ('Sports', 'Sports'),
    ('Spiritual & Mental', 'Spiritual & Mental'),
    ('Travel', 'Travel'),
]

class Hobby(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=25, choices = HOBBY_CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    # user_posts = User.objects.all().annotate(post = Count('post'))
    profile_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

