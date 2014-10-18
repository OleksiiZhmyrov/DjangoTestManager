from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput
from TestManagerCore.utils import CustomErrorList


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.fields['username'].widget = TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Login',
            }
        )
        self.fields['password1'].widget = TextInput(
            attrs={
                'class': 'form-control ',
                'required': '',
                'type': 'password',
                'placeholder': 'Password',
            }
        )
        self.fields['password2'].widget = TextInput(
            attrs={
                'class': 'form-control ',
                'required': '',
                'type': 'password',
                'placeholder': 'Confirm password',
            }
        )


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.fields['username'].widget = TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Login',
            }
        )
        self.fields['password'].widget = TextInput(
            attrs={
                'class': 'form-control ',
                'required': '',
                'type': 'password',
                'placeholder': 'Password',
            }
        )

