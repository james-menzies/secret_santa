from django.core.validators import MinValueValidator, \
    MaxValueValidator
from django.db import models

# Create your models here.
from users.models import CustomUser


class Event(models.Model):
    class EventStatus(models.TextChoices):
        INACTIVE = 'I'
        ACTIVE = 'A'
        CONCLUDED = 'C'

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='event_pictures', null=True, blank=True)
    game_length = models.IntegerField(
        validators=(MinValueValidator(3), MaxValueValidator(60)))
    created_at = models.DateTimeField(auto_now_add=True)
    conclusion = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=EventStatus.choices,
        default=EventStatus.INACTIVE,
    )
    revealed = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, related_name='owned_events', on_delete=models.CASCADE)
    participants = models.ManyToManyField(CustomUser, related_name='events')

    def __str__(self):
        return f"<Event: {self.name}>"


class Gift(models.Model):
    message = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='gifts',
                              related_query_name='gifts')
