from django import forms
from TestManagerCore.models import Environment, Sprint
from TestManagerCore.utils import CustomErrorList
from TestManagerExec.models import TestCaseResult


class TestCaseResultCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestCaseResultCreateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['environment'].widget = forms.Select(
            choices=((i.pk, ', '.join([i.name, i.url])) for i in Environment.objects.all()),
            attrs={
                'class': 'form-control',
                'autofocus': '',
                'required': '',
            },
        )

        self.fields['sprint'].widget = forms.Select(
            choices=((i.pk, i.name) for i in Sprint.objects.all()),
            attrs={
                'class': 'form-control',
                'required': '',
            },
        )

        self.fields['risks'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Assumptions and risks',
            },
        )

    class Meta:
        model = TestCaseResult
        fields = ['environment', 'sprint', 'risks', ]