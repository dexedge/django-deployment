from django.contrib import admin

# Register your models here.
from .models import Date, Event, WorkEvent, Work, Author, AuthorWork, Composer, ComposerWork

admin.site.register(Date)
admin.site.register(Event)
admin.site.register(WorkEvent)
admin.site.register(Work)
admin.site.register(Author)
admin.site.register(AuthorWork)
admin.site.register(Composer)
admin.site.register(ComposerWork)
