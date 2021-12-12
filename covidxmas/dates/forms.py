from django import forms
from .models import Calendar, Date


class DateForm(forms.ModelForm):
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows':2,
            'width':'100%',
            'class': 'form-control',
            'placeholder': 'Enter Image/YouTube Video Url or a text quote'}))

    class Meta:
        model = Date
        fields = ['date', 'content', 'gift']


class CalendarForm(forms.ModelForm):
    name = forms.CharField(
        label="Calendar Name",
        widget=forms.TextInput(attrs={
            'width':'100%',
            'class': 'form-control',
            'placeholder': 'e.g. Alex\'s Calendar'}))
    class Meta:
        model = Calendar
        fields = ['user', 'name', 'days']
