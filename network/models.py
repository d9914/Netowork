from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)


class Post(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()

    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date.strftime('%d %b %Y %H:%M:%S') }"
