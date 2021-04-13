from django.contrib import admin

# Register your models here.
from .models import Date, Event, WorkEvent, Work

admin.site.register(Date)
admin.site.register(Event)
admin.site.register(WorkEvent)
admin.site.register(Work)
