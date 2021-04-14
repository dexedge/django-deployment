from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models

# Create your views here.
class Index(TemplateView):
    """schletter_test home page """
    context_object_name = 'index'
    template_name = 'schletter_test/index.html'

class DateList(ListView):
    context_object_name = 'calendar'
    model = models.Date
    paginate_by = 32
    template_name = 'schletter_test/calendar.html'

class EventList(ListView):
    context_object_name = 'events'
    model = models.Event
    paginate_by = 50
    template_name = 'schletter_test/events.html'

class EventDetail(DetailView):
    context_object_name = 'event'
    model = models.Event
    template_name = 'schletter_test/event.html'

class WorkList(ListView):
    context_object_name = 'works'
    model = models.Work
    paginate_by = 50
    template_name = 'schletter_test/works.html'

class WorkDetail(DetailView):
    context_object_name = 'work'
    model = models.Work
    template_name = 'schletter_test/work.html'