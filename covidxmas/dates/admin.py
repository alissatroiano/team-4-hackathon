from django.contrib import admin
from django.conf import settings
from .models import Date, Calendar

# Register your models here.

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = [
        'calendar', 
        'date', 
        'gift', 
        'content',
	]
    list_filter = ['calendar',]
    search_fields = ['date', 'calendar__name']
    fields = [
		'date', 'calendar', 'content', 'gift'
	]
    
@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
	list_display = [
     'user',
     'name',
     'days',
     'year',
     'is_public',
	]
 
	list_filter = ['user',]
 
	search_fields = ['name', 'user']
 
	fields = [
     'name', 'user', 'days', 'year', 'is_public',
	]