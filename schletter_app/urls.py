"""URLs for schletter_app"""
from django.urls import path
from . import views
from .views import about_view

app_name = 'schletter_app'

urlpatterns = [
    # Home page
    path('', views.Index.as_view(), name='index'),
    # About page
    path('about/', about_view, name  = 'about'),

    # Calendar page
    path('calendar/', views.DateList.as_view(), name='calendar'),
    # Events
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event'),
    path('events/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    # Works
    path('works/', views.WorkList.as_view(), name="works"),
    path('works/<int:pk>', views.WorkDetail.as_view(), name='work'),
    path('works/edit/<int:pk>/', views.WorkEdit.as_view(), name='work_edit'),
    # Authors
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author'),
    path('authors/edit/<int:pk>/', views.AuthorEdit.as_view(), name='author_edit'),

    # Composers
    path('composers/', views.ComposerList.as_view(), name='composers'),
    path('composers/<int:pk>/', views.ComposerDetail.as_view(), name='composer'),
    path('composers/edit/<int:pk>/', views.ComposerEdit.as_view(), name='composer_edit'),
]
