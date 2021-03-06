from django.forms import ModelForm, forms, EmailField, formset_factory, ModelChoiceField, \
    RadioSelect
from django.utils.safestring import mark_safe

from events.models import Event, Gift, Emoji


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'game_length']


class EmailForm(forms.Form):
    email = EmailField(label='Email', required=False)


EmailFormSet = formset_factory(EmailForm, extra=1, min_num=4, max_num=9, validate_max=True)


class ImageChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj

class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['emoji', 'message']

    emoji = ImageChoiceField(queryset=Emoji.objects.all(), widget=RadioSelect)
