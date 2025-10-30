# project/snippets/models.py
from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    title = models.CharField(max_length=200)
    code = models.TextField()
    language = models.CharField(max_length=50, default='python')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title