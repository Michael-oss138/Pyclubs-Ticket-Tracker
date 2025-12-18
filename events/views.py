from django.shortcuts import render
from .models import Event, Semester

# Create your views here.


def event_list(request):
    semester = Semester.get_current()
    if not semester:
        return render (request, "no_semester.html")
    events = Event.objects.filter(semester=semester, is_active=True)
    return render(request, "event_list.html", {"events": events, "semester": semester})