from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.

class TicketSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticket_selections")
    event = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_selections")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + self.event.title
