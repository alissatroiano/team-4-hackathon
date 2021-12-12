from django.urls import path
from .views import create_calendar, edit_calendar, view_calendars


urlpatterns = [
    path('create_calendar/', create_calendar, name='create_calendar'),
    path('edit_calendar/', edit_calendar, name='edit_calendar'),
    path('view_calendars/', view_calendars, name='view_calendars'),
]