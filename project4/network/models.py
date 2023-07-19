from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField("self", blank=True)
    followers = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user_id")
    content = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    comments = models.ManyToManyField("Comment", related_name="post_comment", blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_formatted_date()

    def get_formatted_date(self):
        return self.date.strftime("%B %d, %Y, %I:%M %p")

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user_id")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post_id")
    content = models.CharField(max_length=100)
    likes = models.IntegerField()
    date = models.DateField(auto_now_add=True)