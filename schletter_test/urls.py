"""URLs for schletter_test"""
from django.urls import path
from . import views

app_name = 'schletter_test'

urlpatterns = [
    # Home page
    path('', views.Index.as_view(), name='index'),
    # Events page
    path('events/', views.EventList.as_view(), name='events'),
    # Event detail page
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event')
]
