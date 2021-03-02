from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='event_pictures', null=True, blank=True)
    time = models.DateTimeField()
    active = models.BooleanField(default=False)
    revealed = models.BooleanField(default=True)



class Gift(models.Model):

    message = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='gifts',
                              related_query_name='gifts')
