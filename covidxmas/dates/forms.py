from django.forms.models import ModelForm
from .models import Calendar, Date


class DateForm(ModelForm):
	class Meta:
		model = Date
		fields = ['date', 'content', 'gift']


class EditCalendarForm(ModelForm):
    class Meta:
        model = Calendar
        fields = ['user', 'name', 'days']