from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from schletter_app.models import Date, Event, Work, Author, Composer

# Create your views here.
class Index(TemplateView):
    """schletter_app home page """
    context_object_name = 'index'
    template_name = 'schletter_app/index.html'

class DateList(ListView):
    context_object_name = 'calendar'
    model = Date
    paginate_by = 40
    template_name = 'schletter_app/calendar.html'
    
    def get_queryset(self):
        date_min = self.request.GET.get('date_min')
        date_max = self.request.GET.get('date_max')
        if date_min is not None and date_max is not None:
            return Date.objects.all().filter(date__gte=date_min, date__lte=date_max)
        else:
            return Date.objects.all()
    
class EventList(ListView):
    context_object_name = 'events'
    model = Event
    paginate_by = 50
    template_name = 'schletter_app/events.html'

class EventDetail(DetailView):
    context_object_name = 'event'
    model = Event
    template_name = 'schletter_app/event.html'

class WorkList(ListView):
    context_object_name = 'works'
    model = Work
    paginate_by = 50
    template_name = 'schletter_app/works.html'

class WorkDetail(DetailView):
    context_object_name = 'work'
    model = Work
    template_name = 'schletter_app/work.html'

class AuthorList(ListView):
    context_object_name = 'authors'
    model = Author
    paginate_by = 50
    template_name = 'schletter_app/authors.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Author.objects.filter(Q(last_name__icontains=query) | Q(first_names__icontains=query))
        else:
            return Author.objects.all()
    
    
class AuthorDetail(DetailView):
    context_object_name = 'author'
    model = Author
    template_name = 'schletter_app/author.html'

class ComposerList(ListView):
    context_object_name = 'composers'
    model = Composer
    paginate_by = 50
    template_name = 'schletter_app/composers.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Composer.objects.exclude(last_name="NA").filter(Q(last_name__icontains=query) | Q(first_names__icontains=query))
        else:
            return Composer.objects.exclude(last_name="NA")

class ComposerDetail(DetailView):
    context_object_name = 'composer'
    model = Composer
    template_name = 'schletter_app/composer.html'