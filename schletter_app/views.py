from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from schletter_app.models import Date, Event, Work, Author, Composer

# Create your views here.
class Index(TemplateView):
    """schletter_app home page """
    context_object_name = 'index'
    template_name = 'schletter_app/index.html'

# Calendar
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
    
# Events
class EventList(ListView):
    context_object_name = 'events'
    paginate_by = 50
    template_name = 'schletter_app/events.html'
    # Value lists for drop downs in Event search
    extra_context = {
        'companies': Event.objects.all().order_by('company').values_list('company', flat=True).distinct(),
        'event_types': Event.objects.all().order_by('event_type').values_list('event_type', flat=True).distinct(),
        'genres': Work.objects.all().order_by('genre').values_list('genre', flat=True).distinct()
        }

    def get_queryset(self):
        qs = Event.objects.all()
        theater = self.request.GET.get('theater')
        company = self.request.GET.get('company')
        event_type = self.request.GET.get('event_type')
        genre = self.request.GET.get('genre')
        if theater is not None and theater != "":
            qs = qs.filter(theater=theater)
        if company is not None and company != "":
            qs = qs.filter(company=company)
        if event_type is not None and event_type != "":
            qs = qs.filter(event_type=event_type)
        if genre is not None and genre != "":
            qs = qs.filter(work__genre=genre)
        return qs

class EventDetail(DetailView):
    context_object_name = 'event'
    model = Event
    template_name = 'schletter_app/event.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context

# Works
class WorkQueryMixin:
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Work.objects.filter(Q(title__icontains=query) | Q(genre__icontains=query))
        else:
            return Work.objects.all()

class WorkList(WorkQueryMixin, ListView):
    context_object_name = 'works'
    model = Work
    paginate_by = 50
    template_name = 'schletter_app/works.html'

class WorkDetail(WorkQueryMixin, DetailView):
    context_object_name = 'work'
    model = Work
    template_name = 'schletter_app/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prev_pk = (
            self.get_queryset()
            .filter(sort_title__lt=self.object.sort_title)
            .reverse().values('pk')[:1]
        )
        # There may be no next page
        if prev_pk:
            context['prev_pk'] = prev_pk[0]['pk']
        
        next_pk = (
            self.get_queryset()
            .filter(sort_title__gt=self.object.sort_title)
            .values('pk').values('pk')[:1]
        )
        # There may be no next page
        if next_pk:
            context['next_pk'] = next_pk[0]['pk']
        
        return context

# Authors
class AuthorQueryMixin:
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Author.objects.filter(Q(last_name__icontains=query) | Q(first_names__icontains=query))
        else:
            return Author.objects.all()

class AuthorList(AuthorQueryMixin, ListView):
    context_object_name = 'authors'
    model = Author
    paginate_by = 50
    template_name = 'schletter_app/authors.html'

class AuthorDetail(AuthorQueryMixin, DetailView):
    context_object_name = 'author'
    model = Author
    template_name = 'schletter_app/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prev_pk = (
            self.get_queryset()
            .filter(last_name__lt=self.object.last_name)
            .reverse().values('pk')[:1]
        )
        # There may be no next page
        if prev_pk:
            context['prev_pk'] = prev_pk[0]['pk']
        
        next_pk = (
            self.get_queryset()
            .filter(last_name__gt=self.object.last_name)
            .values('pk').values('pk')[:1]
        )
        # There may be no next page
        if next_pk:
            context['next_pk'] = next_pk[0]['pk']
        
        return context

# Composers
class ComposerQueryMixin:
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Composer.objects.exclude(last_name="NA").filter(Q(last_name__icontains=query) | Q(first_names__icontains=query))
        else:
            return Composer.objects.all().exclude(last_name="NA")

class ComposerList(ComposerQueryMixin, ListView):
    context_object_name = 'composers'
    model = Composer
    paginate_by = 50
    template_name = 'schletter_app/composers.html'

class ComposerDetail(ComposerQueryMixin, DetailView):
    context_object_name = 'composer'
    model = Composer
    template_name = 'schletter_app/composer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prev_pk = (
            self.get_queryset()
            .filter(last_name__lt=self.object.last_name)
            .reverse().values('pk')[:1]
        )
        # There may be no next page
        if prev_pk:
            context['prev_pk'] = prev_pk[0]['pk']
        
        next_pk = (
            self.get_queryset()
            .filter(last_name__gt=self.object.last_name)
            .values('pk').values('pk')[:1]
        )
        # There may be no next page
        if next_pk:
            context['next_pk'] = next_pk[0]['pk']
        
        return context