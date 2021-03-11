from events.models import Event


def conclude_event(event_id):
    event = Event.objects.get(event_id)
    event.status = Event.EventStatus.CONCLUDED
    event.save()
