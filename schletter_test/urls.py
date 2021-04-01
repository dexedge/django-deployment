"""URLs for schletter_test"""
from django.urls import path
from . import views

app_name = 'schletter_test'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Events page
    path('events/', views.events, name='events'),
    # Event detail page
    path('events/<int:event_id>/', views.event, name='event')
]
