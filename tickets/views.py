from django.shortcuts import render, redirect, get_object_or_404
from .models import TicketSelection
from events.models import Event
from  django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def select_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)


    TicketSelection.objects.get_or_create(
        user = request.user
        event=event
    )
        
    return redirect("my_events")

def my_events(request):
    selections = TicketSelection.objects.filter(user=request.user)
    return render(request, "tickets/my_events.html", {"selections": selections})
