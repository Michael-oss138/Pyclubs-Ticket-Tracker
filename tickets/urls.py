from django.urls import path
from .views import select_event, my_events

urlpatterns = [
        path("select/<int:event_id>/", select_event, name="select_event"),
        path("my-events/", my_events, name="my_events"),
]
