from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def calendar(request, calendar_id):
    return render(request, 'calendar.html')


def calendar_start(request):
    return render(request, 'calendar-start.html')