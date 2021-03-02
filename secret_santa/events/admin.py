from django.contrib import admin

# Register your models here.
from events.models import Event, Gift

admin.site.register(Event)
admin.site.register(Gift)
