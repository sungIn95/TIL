from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    running_time = models.IntegerField()
