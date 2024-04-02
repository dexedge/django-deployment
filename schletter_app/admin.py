from typing import Any
from django.contrib import admin
from django.db.models import Count

# Register your models here.
from .models import About, Date, Event, WorkEvent, Work, Author, AuthorWork, Composer, ComposerWork
from adminsortable2.admin import SortableAdminMixin

class DateAdmin(admin.ModelAdmin):
    ordering = ('date',)
    date_hierarchy = 'date'

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'performances')
    ordering = ('title', 'genre')
    list_filter = ('genre',)
    search_fields = ('title',)

    def get_queryset(self, request):
        queryset= super().get_queryset(request)
        print(queryset)
        queryset = queryset.annotate(
            _performances = Count("events", distinct=True)
        )
        return queryset
    
    def performances(self, obj):
        return obj.events.count()
    
    performances.admin_order_field = "_performances"

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_names', 'birth', 'death')
    ordering = ('last_name', 'birth', 'death')
    search_fields = ('last_name',)

class ComposerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_names', 'birth', 'death')
    ordering = ('last_name', 'birth', 'death')
    search_fields = ('last_name',)


admin.site.register(About)
admin.site.register(Date, DateAdmin)
# admin.site.register(Event)
admin.site.register(WorkEvent)
admin.site.register(Work, WorkAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorWork)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(ComposerWork)

@admin.register(Event)
class SortableEventAdmin(SortableAdminMixin, admin.ModelAdmin):
   list_display = ('date', 'title', 'theater', 'company')
   list_filter = ('theater', 'company')
   search_fields = ('title',)

