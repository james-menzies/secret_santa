from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Column, Row, Submit
from django.forms import ModelForm, forms, EmailField, formset_factory, ModelChoiceField, \
    RadioSelect
from django.utils.safestring import mark_safe

from events.models import Event, Gift, Emoji


class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'col-md-6'
        self.helper.layout = Layout(
            'name',
            'game_length',
            'image',
            'description',
        )
        self.helper.form_tag = False

    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'game_length']


class EmailForm(forms.Form):
    email = EmailField(label='Email', required=False)


EmailFormSet = formset_factory(EmailForm, extra=1, max_num=9, validate_max=True)


class EmailFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_tag = False
        self.disable_csrf = True


class ImageChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj


class RadioImageControl(Field):
    template = 'image_radio.html'


class GiftForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'col-md-6'
        self.helper.layout = Layout(
            'message',
            RadioImageControl('emoji',),
            Submit("submit", "Give", )
        )

    class Meta:
        model = Gift
        fields = ['emoji', 'message']

    emoji = ImageChoiceField(queryset=Emoji.objects.all(), widget=RadioSelect)
