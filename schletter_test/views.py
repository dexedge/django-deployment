from django.shortcuts import render
from .models import Event

# Create your views here.
def index(request):
    """schletter_test home page """
    return render(request, 'schletter_test/index.html')

def events(request):
    """Show all events"""
    events = Event.objects.order_by('date')
    context = {'events': events}
    return render(request, 'schletter_test/events.html', context)

def event(request, event_id):
    """Show detail on single event"""
    event = Event.objects.get(id=event_id)
    context = {'event': event}
    return render(request, 'schletter_test/event.html', context)