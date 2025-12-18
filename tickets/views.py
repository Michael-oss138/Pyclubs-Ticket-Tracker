from django.shortcuts import render, redirect, get_object_or_404
from .models import TicketSelection
from events.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def select_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if TicketSelection.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, "You are already registered for this event.")
        return redirect("my_events")

    if TicketSelection.objects.filter(event=event).count() >= event.capacity:
        messages.error(request, "This event is fully booked.")
        return redirect("my_events")

    TicketSelection.objects.create(
        user=request.user,
        event=event
    )
    
    messages.success(request, "You have successfully registered for the event!")
    return redirect("my_events")


@login_required
def my_events(request):
    selections = TicketSelection.objects.filter(user=request.user)
    return render(request, "tickets/my_events.html", {"selections": selections})
