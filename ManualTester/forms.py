from django import forms

from ManualTester.models import TestSuite, TestCase, OrderTestCase, TestCaseStatus
from TestManagerCore.models import Tag
from TestManagerCore.utils import CustomErrorList


class TestSuiteCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestSuiteCreateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Name',
            },
        )

        self.fields['description'].widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Verbose description',
            },
        )

    class Meta:
        model = TestSuite
        fields = ['name', 'description', ]


class TestSuiteUpdateForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(TestSuiteUpdateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Name',
            },
        )

        self.fields['description'].widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Verbose description',
            },
        )

    class Meta:
        model = TestSuite
        fields = ['name', 'description', 'tags', ]


class OrderTestCaseCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderTestCaseCreateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['number'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Integer value',
            },
        )

        self.fields['test_case'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestCase.objects.all()),
            attrs={
                'class': 'form-control',
            },
        )

    class Meta:
        model = OrderTestCase
        fields = ['number', 'test_case', ]


class OrderTestCaseModifyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderTestCaseModifyForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['number'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Integer value',
            },
        )

        self.fields['test_case'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestCase.objects.all()),
            attrs={
                'class': 'form-control',
            },
        )

    class Meta:
        model = OrderTestCase
        fields = ['number', 'test_case', ]


class TestCaseCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestCaseCreateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Name',
            },
        )

        self.fields['description'].widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Verbose description',
            },
        )

        self.fields['status'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestCaseStatus.objects.all()),
            attrs={
                'class': 'form-control',
            },
        )

    class Meta:
        model = TestCase
        fields = ['name', 'description', 'status', ]
