from django.db import models
from datetime import datetime

# Create your models here.

class Date(models.Model):
    date = models.DateField(primary_key=True)

    def __str__(self):
        date = self.date.strftime('%a, %-d %b %Y')
        return date

class Event(models.Model):
    """Schletter Event model"""
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    theater = models.CharField(max_length=3)
    company = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        event = str(self.date) + ", " + self.title
        return event 
