from django.forms import ModelForm, forms, EmailField, formset_factory, IntegerField, CharField

from events.models import Event


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'description', 'image']


class EmailForm(forms.Form):

    email = EmailField(label='Email')

EmailFormSet = formset_factory(EmailForm, extra=1)
