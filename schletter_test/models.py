from django.db import models
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.

class Date(models.Model):
    date = models.DateField(primary_key=True)

    def __str__(self):
        date = self.date.strftime('%a, %-d %b %Y')
        return date

class Event(models.Model):
    """Schletter Event model"""
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    theater = models.CharField(max_length=3)
    company = models.CharField(max_length=10)
    event_type = models.CharField(max_length=50)
    hadamowsky = models.CharField(max_length=5)
    morrow = models.CharField(max_length=5)
    notes = HTMLField(blank=True)
    
    class Meta:
        ordering = ['date', 'theater']
    
    def __str__(self):
        event = str(self.date) + ", " + self.title
        return event

class Work(models.Model):
    events = models.ManyToManyField(Event, through="WorkEvent")
    title = models.CharField(max_length=100)
    sort_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    notes = HTMLField()
    url = models.URLField(max_length=200)
    author = models.CharField(max_length=100)
    composer = models.CharField(max_length=100) 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort_title']

class WorkEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)



