from django.contrib import admin
from .models import Semester, Event

# Register your models here.

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'is_active']
    list_filter = ['is_active']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'semester', 'date', 'capacity', 'is_active']
    list_filter = ['semester', 'is_active']
