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


# def events(request):
#     """Show all events"""
#     events = Event.objects.order_by('date')
#     context = {'events': events}
#     return render(request, 'schletter_test/events.html', context)

# def event(request, event_id):
#     """Show detail on single event"""
#     event = Event.objects.get(id=event_id)
#     context = {'event': event}
#     return render(request, 'schletter_test/event.html', context)