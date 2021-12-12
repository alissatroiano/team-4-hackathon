from django.core.files.base import ContentFile
from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.forms.models import modelformset_factory
from .models import Date, Calendar
from .forms import CalendarForm, DateForm

# Create your views here.
def create_dates(request):
    """ A view to create a new calendar """
    if request.method == 'GET':
        formset = modelformset_factory(Date, form=DateForm, extra=24)
        return render(request, 'edit_dates.html', {'formset': formset})
    else:
        # formset = modelformset_factory(
        #         Date, fields=('date', 'display_name', 'mentor'),
        #         form=HackTeamForm, extra=0)
        return


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
            print(request.POST)
            print(form.errors)
            return render(request, 'create_calendar.html', {'form': form})

        



def view_calendars(request):
    """ A view to return all calendars """
    calendars = Calendar.objects.all()
    
    return render(request, 'view_calendars.html', {'calendars': calendars})


# The edit calendar view is currently broken :(
@login_required
def edit_calendar(request, calendar_id):
    """ A view to edit an existing calendar """
    calendar = get_object_or_404(Calendar, unique_id=calendar_id)
    print(calendar.unique_id)
    CalendarFormSet = modelformset_factory(
        Date, fields=('date', 'gift', 'content'),
        form=DateForm, extra=0)
    
    if request.method == 'GET':
        formset = CalendarFormSet(queryset=Date.objects.filter(calendar=calendar))
        return render(request, 'edit_dates.html', {'formset': formset})
    else:
        formset = CalendarFormSet(request.POST, queryset=Date.objects.filter(calendar=calendar))
        print(formset.errors)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('view_calendars'))
        else:
            return render(request, 'edit_dates.html', {'formset': formset})
        
        

