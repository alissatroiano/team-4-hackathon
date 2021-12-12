from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.forms.models import modelformset_factory
from .models import Date, Calendar
from .forms import DateForm

# Create your views here.
def create_calendar(request):
    """ A view to create a new calendar """
    if request.method == 'GET':
        formset = modelformset_factory(Date, form=DateForm, extra=24)
        
        return render(request, 'create_calendar.html', {'formset': formset})


def view_calendars(request):
    """ A view to return all calendars """
    calendars = Calendar.objects.all()
    
    return render(request, 'view_calendars.html', {'calendars': calendars})


@login_required
def edit_calendar(request, calendar_id):
    """ A view to edit an existing calendar """
    calendar = get_object_or_404(Calendar, pk=calendar_id)
    
    if request.method == 'POST':
        form = DateForm(request.POST, instance=calendar)
        if form.is_valid():
            form.save()
            return redirect('view_calendars')
    
    return render(request, 'edit_calendar.html', {'calendar': calendar})
