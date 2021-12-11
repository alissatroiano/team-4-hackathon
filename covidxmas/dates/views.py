from django.shortcuts import render
from django.forms.models import modelformset_factory
from .models import Date
from .forms import DateForm

# Create your views here.
def create_calendar(request):
    if request.method == 'GET':
        formset = modelformset_factory(Date, form=DateForm, extra=24)
        
        return render(request, 'create_calendar.html', {'formset': formset})

def view_calendars(request):
    return render(request, 'view_calendars.html')

def edit_calendar(request):
    return render(request, 'edit_calendar.html')
