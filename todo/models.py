from django.db import models
from django.urls import reverse

class Post(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text=models.TextField()

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.text[:50]

