from django.contrib.admin import widgets
from django.forms import ModelForm, forms, EmailField, formset_factory, DateTimeField

from events.models import Event


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'game_length']



class EmailForm(forms.Form):

    email = EmailField(label='Email', required=False)

EmailFormSet = formset_factory(EmailForm, extra=1, min_num=4, max_num=9, validate_max=True)
