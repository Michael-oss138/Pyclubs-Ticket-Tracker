from django.core.mail import send_mail, EmailMessage
from django.utils import timezone
from events.models import Event
from .models import TicketSelection
from datetime import timedelta
from io import BytesIO
from reportlab.pdfgen import canvas



def generate_ticlet_pdf(ticket):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=(200, 150))

    c.setFont("Helvetica-Bold", 14)
    c.drawString(20, 220, f"Event: {ticket.event.title}")
    c.setFont("Helvetica", 12)
    c.drawString(20, 200, f"Name: {ticket.user.get_full_name() or ticket.user.username}")
    c.drawString(20, 180, f"Date: {ticket.event.date}")
    c.drawString(20, 160, f"Ticket ID: {ticket.id}")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer  

def send_ticket_notifications():
    today = timezone.now().date()
    notify_date = today + timedelta(days=1)

    # Get events happening in 30 days
    events = Event.objects.filter(date=notify_date, is_active=True)

    for event in events:
        selections = TicketSelection.objects.filter(event=event)
        for selection in selections:
            pdf_buffer = generate_ticlet_pdf(selection)

            email = EmailMessage(
                subject=f"Your ticket for {event.title} is ready",
                body=f"Hi {selection.user.first_name},\n\nYou can now collect your ticket for the event '{event.title}' happening on {event.date}.\n\nThanks!",
                from_email=None,
                to=[selection.user.email],
            )
            email.attach(f"ticket_{selection.id}.pdf", pdf_buffer.getvalue(), "application/pdf")
            email.send()
