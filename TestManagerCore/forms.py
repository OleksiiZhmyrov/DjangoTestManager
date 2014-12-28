from TestManagerCore.models import UserProfile, Project
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from TestManagerCore.utils import CustomErrorList


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Login',
            }
        )
        self.fields['password1'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'required': '',
                'type': 'password',
                'placeholder': 'Password',
            }
        )
        self.fields['password2'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'required': '',
                'type': 'password',
                'placeholder': 'Confirm password',
            }
        )

    def save(self, *args, **kwargs):
        user = super(UserRegistrationForm, self).save(*args, **kwargs)
        profile = UserProfile(
            user=user,
        )
        profile.save()
        profile.projects.add(
            Project.objects.get(pk=1),
        )
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Login',
            }
        )
        self.fields['password'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'required': '',
                'type': 'password',
                'placeholder': 'Password',
            }
        )


class UserUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['first_name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'First name',
            }
        )

        self.fields['last_name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Last name',
            }
        )

        self.fields['email'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'e-mail address',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]


class UserProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['default_project'].widget = forms.Select(
            choices=((i.pk, i.name) for i in self.instance.projects.all()),
            attrs={
                'class': 'form-control',
            },
        )

    class Meta:
        model = UserProfile
        fields = ['default_project', ]
