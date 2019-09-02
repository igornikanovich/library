from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.pk)])


class Book(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='books')
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title
