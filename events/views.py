from django.shortcuts import render
from .models import Event
from .models import get_current_semester

# Create your views here.

def event_list(request):
    semester = get_current_semester()
    if not semester:
        return render (request, "no_semester.html")
    events = Event.objects.filter(semester=semester)
    return render(request, "event_list.html", {"events": events})