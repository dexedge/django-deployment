"""URLs for schletter_app"""
from django.urls import path
from . import views

app_name = 'schletter_app'

urlpatterns = [
    # Home page
    path('', views.Index.as_view(), name='index'),
    # Calendar page
    path('calendar/', views.DateList.as_view(), name='calendar'),
    # Events page
    path('events/', views.EventList.as_view(), name='events'),
    # Event detail page
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event'),
    # Works page
    path('works/', views.WorkList.as_view(), name="works"),
    # Work detail page
    path('works/<int:pk>', views.WorkDetail.as_view(), name='work'),
    # Authors page
    path('authors/', views.AuthorList.as_view(), name='authors'),
    # Author detail page
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author'),
    # Composers page
    path('composers/', views.ComposerList.as_view(), name='composers'),
    # Composer detail page
    path('composers/<int:pk>/', views.ComposerDetail.as_view(), name='composer'),
]
