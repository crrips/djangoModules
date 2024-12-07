from django.db import models
from django.contrib.auth.models import AbstractUser


class Site_User(AbstractUser):
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Site_User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    upvoters = models.ManyToManyField(Site_User, related_name='upvoters')
    downvoters = models.ManyToManyField(Site_User, related_name='downvoters')
    

    def __str__(self):
        return self.content