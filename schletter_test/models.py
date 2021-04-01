from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    """Simple model for Schletter flat file"""
    date = models.DateField()
    theater = models.CharField(max_length=3)
    company = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)

    def __str__(self):
        event = self.date.strftime('%a, %-d %b %Y') + " " + self.title
        return event
