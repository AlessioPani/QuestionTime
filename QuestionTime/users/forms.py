from .models import CustomUser
from django_registration.forms import RegistrationForm


class CustomUserForm(RegistrationForm):
    '''
    Registration form used on registration
    template.

    * Uses a CustomUser model.
    '''
    class Meta(RegistrationForm.Meta):
        model = CustomUser
