from django.urls import path
from .views import create_calendar, edit_dates, view_calendars, settings, view_public_calendars


urlpatterns = [
    path('create_calendar/', create_calendar, name='create_calendar'),
    path('edit_dates/<str:calendar_id>/', edit_dates, name='edit_dates'),
    path('settings/<str:calendar_id>/', settings, name='settings'),
    path('view_calendars/', view_calendars, name='view_calendars'),
    path('view_public_calendars/', view_public_calendars, name='view_public_calendars'),
]