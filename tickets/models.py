from django.db import models
from django.contrib.auth.models import User
from events.models import Events

# Create your models here.

class TicketSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + self.event.title
