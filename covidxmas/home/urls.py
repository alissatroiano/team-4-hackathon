from django.urls import path

from .views import home, calendar, calendar_start


urlpatterns = [
    path('', home, name='home'),
    path('calendar/', calendar, name='calendar'),
    path('calendar-start/', calendar_start, name='calendar_start'),
]