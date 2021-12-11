from django.urls import path

from .views import create_calendar


urlpatterns = [
    path('create_calendar/', create_calendar, name='create_calendar'),
    path('edit_calendar/', create_calendar, name='edit_calendar'),
]