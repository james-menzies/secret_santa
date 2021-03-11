from django.contrib import admin

# Register your models here.
from events.models import Event, Gift, Emoji

admin.site.register(Event)
admin.site.register(Gift)
admin.site.register(Emoji)
