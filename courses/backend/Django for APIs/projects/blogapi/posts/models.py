from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # user django default user as author, we specify it as ForeignKey
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
