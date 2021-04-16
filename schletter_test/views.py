from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from schletter_test.models import Date, Event, Work, Author, Composer

# Create your views here.
class Index(TemplateView):
    """schletter_test home page """
    context_object_name = 'index'
    template_name = 'schletter_test/index.html'

class DateList(ListView):
    context_object_name = 'calendar'
    model = Date
    paginate_by = 40
    template_name = 'schletter_test/calendar.html'

class EventList(ListView):
    context_object_name = 'events'
    model = Event
    paginate_by = 50
    template_name = 'schletter_test/events.html'

class EventDetail(DetailView):
    context_object_name = 'event'
    model = Event
    template_name = 'schletter_test/event.html'

class WorkList(ListView):
    context_object_name = 'works'
    # Omit first Work, which is "NA"
    queryset = Work.objects.all()[1:]
    paginate_by = 50
    template_name = 'schletter_test/works.html'

class WorkDetail(DetailView):
    context_object_name = 'work'
    model = Work
    template_name = 'schletter_test/work.html'

class AuthorList(ListView):
    context_object_name = 'authors'
    model = Author
    paginate_by = 50
    template_name = 'schletter_test/authors.html'

class AuthorDetail(DetailView):
    context_object_name = 'author'
    model = Author
    template_name = 'schletter_test/author.html'

class ComposerList(ListView):
    context_object_name = 'composers'
    model = Composer
    paginate_by = 50
    template_name = 'schletter_test/composers.html'

class ComposerDetail(DetailView):
    context_object_name = 'composer'
    model = Composer
    template_name = 'schletter_test/composer.html'

