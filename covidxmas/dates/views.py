from django.core.files.base import ContentFile
from django.db.models.fields import PositiveBigIntegerField
from django.http import request
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.forms.models import modelformset_factory
from .models import Date, Calendar
from .forms import CalendarForm, DateForm


@login_required
def settings(request, calendar_id):
    """ A view to create a new calendar """
    calendar = get_object_or_404(Calendar, unique_id=calendar_id)
    previous_days = calendar.days
    if request.method == 'GET':
        form = CalendarForm(instance=calendar)
        return render(request, 'create_calendar.html', {'form': form})
    else:
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            calendar = form.save()
            if previous_days > int(request.POST.get('days')):
                date = Date.objects.filter(date=25, calendar=calendar)
                date.delete()
            elif previous_days < int(request.POST.get('days')):
                date = Date(calendar=calendar, date=25)
                date.save()
            return redirect(reverse('view_calendars'))
        else:
            print(form.errors)
            return render(request, 'create_calendar.html', {'form': form})


@login_required
def create_calendar(request):
    """ A view to create a new calendar """
    if request.method == 'GET':
        form = CalendarForm()
        return render(request, 'create_calendar.html', {'form': form})
    else:
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save()
            for day in range(1, int(request.POST.get('days'))+1):
                # Create an empty Date per day in days selected when Calendar
                # is created
                Date.objects.create(calendar=calendar, date=day)
            return redirect(reverse('view_calendars'))
        else:
            print(form.errors)
            return render(request, 'create_calendar.html', {'form': form})


@login_required
def view_calendars(request):
    """ A view to return all calendars """
    calendars = Calendar.objects.filter(user=request.user)    
    return render(request, 'view_calendars.html', {'calendars': calendars})


@login_required
def edit_dates(request, calendar_id):
    """ A view to edit an existing calendar """
    calendar = get_object_or_404(Calendar, unique_id=calendar_id)
    CalendarFormSet = modelformset_factory(
        Date, fields=('date', 'gift', 'content'),
        form=DateForm, extra=0)
    
    if request.method == 'GET':
        formset = CalendarFormSet(queryset=Date.objects.filter(calendar=calendar))
        return render(request, 'edit_dates.html', {'formset': formset})
    else:
        formset = CalendarFormSet(request.POST, queryset=Date.objects.filter(calendar=calendar))
        if formset.is_valid():
            formset.save()
            return redirect(reverse('view_calendars'))
        else:
            formset = CalendarFormSet(queryset=Date.objects.filter(calendar=calendar))
            return render(request, 'edit_dates.html', {'formset': formset})


@login_required
def delete_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, unique_id=calendar_id)
    
    if request.user == calendar.user:
        calendar.delete()
        return redirect(reverse('view_calendars'))


def view_public_calendars(request):
    calendars = Calendar.objects.filter(is_public=True).order_by('?')
    return render(request, 'view_public_calendars.html', {'calendars': calendars})
