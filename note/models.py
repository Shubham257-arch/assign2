# note/models.py
from django.db import models
from users.models import User  # Correct import


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to custom User model

    def __str__(self):
        return self.title
