from django.core.mail import send_mail
from django.utils import timezone
from events.models import Event
from .models import TicketSelection
from datetime import timedelta

def send_ticket_notifications():
    today = timezone.now().date()
    notify_date = today + timedelta(days=1)

    # Get events happening in 30 days
    events = Event.objects.filter(date=notify_date, is_active=True)

    for event in events:
        selections = TicketSelection.objects.filter(event=event)
        for selection in selections:
            send_mail(
                subject=f"Your ticket for {event.title} is ready",
                message=f"Hi {selection.user.first_name},\n\nYou can now collect your ticket for the event '{event.title}' happening on {event.date}.\n\nThanks!",
                from_email=None,  # uses DEFAULT_FROM_EMAIL
                recipient_list=[selection.user.email],
            )
