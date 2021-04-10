from django.contrib import admin

# Register your models here.
from .models import Date, Event

admin.site.register(Date)
admin.site.register(Event)
