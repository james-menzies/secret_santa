from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'display_name', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'col-md'
        self.helper.form_show_errors = True
        self.helper.form_id = 'id-registration-form'
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class='btn btn-lg btn-primary btn-block'))




class UserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['display_name', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'col-md'
        self.helper.form_show_errors = True
        self.helper.form_id = 'id-registration-form'
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class='btn btn-lg btn-primary btn-block'))
