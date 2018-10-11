from django.contrib.auth.models import User
from django.db import models


class KeyWord(models.Model):
    word = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        self.word = self.word.lower()
        return super(KeyWord, self).save(*args, **kwargs)

    def __str__(self):
        return self.word


class Video(models.Model):
    title = models.CharField(max_length=128)
    keywords = models.ManyToManyField(KeyWord)
    url = models.URLField(max_length=128, unique=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
