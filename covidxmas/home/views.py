from django.shortcuts import get_object_or_404, render

from dates.models import Calendar


def home(request):
    return render(request, 'index.html')


def calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, unique_id=calendar_id)
    dates = calendar.dates.order_by('date')
    return render(request, 'calendar.html', {'calendar': calendar, 'dates': dates})


def calendar_start(request):
    return render(request, 'calendar-start.html')