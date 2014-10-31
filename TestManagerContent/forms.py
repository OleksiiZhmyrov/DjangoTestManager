from django import forms
from django.template.defaultfilters import filesizeformat
from DjangoTestManager.settings import CONTENT_TYPES, MAX_UPLOAD_SIZE

from TestManagerContent.models import TestSuite, TestCase, OrderTestCase, TestCaseStatus, TestStep, OrderTestStep, \
    TestStepStatus
from TestManagerCore.models import Tag, Screenshot, ApplicationFeature
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


class TestCaseUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(TestCaseUpdateForm, self).__init__(*args, **kwargs)
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
        fields = ['name', 'description', 'status', 'tags', ]


class OrderTestStepCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderTestStepCreateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['number'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Integer value',
            },
        )

        self.fields['test_step'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestStep.objects.all()),
            attrs={
                'class': 'form-control',
                'size': '10',
            },
        )

    class Meta:
        model = OrderTestStep
        fields = ['number', 'test_step', ]


class OrderTestStepModifyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderTestStepModifyForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['number'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Integer value',
            },
        )

        self.fields['test_step'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestStep.objects.all()),
            attrs={
                'class': 'form-control',
                'size': '10',
            },
        )

    class Meta:
        model = OrderTestStep
        fields = ['number', 'test_step', ]


class TestStepCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestStepCreateForm, self).__init__(*args, **kwargs)
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

        self.fields['expected_result'].widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Expected result',
            },
        )

        self.fields['application_feature'].widget = forms.Select(
            choices=((i.pk, i.name) for i in ApplicationFeature.objects.all()),
            attrs={
                'class': 'form-control',
                'required': '',
            },
        )

        self.fields['status'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestStepStatus.objects.all()),
            attrs={
                'class': 'form-control',
            },
        )

    class Meta:
        model = TestStep
        fields = ['name', 'description', 'expected_result', 'application_feature', 'status', ]


class TestStepUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(TestStepUpdateForm, self).__init__(*args, **kwargs)
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

        self.fields['expected_result'].widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Expected result',
            },
        )

        self.fields['application_feature'].widget = forms.Select(
            choices=((i.pk, i.name) for i in ApplicationFeature.objects.all()),
            attrs={
                'class': 'form-control',
                'required': '',
            },
        )

        self.fields['status'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestStepStatus.objects.all()),
            attrs={
                'class': 'form-control',
            },
        )

        self.fields['screenshot'].widget = forms.Select(
            choices=self._get_screenshots_tupple(),
            attrs={
                'class': 'form-control',
            },
        )

    @staticmethod
    def _get_screenshots_tupple():
        screenshot_queryset = Screenshot.objects.all()
        screenshots = [('', 'none')] + [(i.pk, i.name) for i in screenshot_queryset]
        return list(screenshots)

    class Meta:
        model = TestStep
        fields = ['name', 'description', 'expected_result', 'application_feature', 'status', 'tags', 'screenshot', ]


class ScreenshotCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScreenshotCreateForm, self).__init__(*args, **kwargs)
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

    def clean_screenshot(self):
        screenshot = self.cleaned_data['screenshot']
        if screenshot:
            content_type = screenshot.content_type
            if content_type in CONTENT_TYPES:
                if screenshot.size > MAX_UPLOAD_SIZE:
                    raise forms.ValidationError('Please keep file size under %s. Current file size %s' % (
                        filesizeformat(MAX_UPLOAD_SIZE), filesizeformat(screenshot.size)))
            else:
                raise forms.ValidationError('File type is not supported. Supported types are: %s' % ','.join(CONTENT_TYPES))
        return screenshot

    class Meta:
        model = Screenshot
        fields = ['name', 'description', 'screenshot', ]


class ScreenshotUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ScreenshotUpdateForm, self).__init__(*args, **kwargs)
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
        model = TestStep
        fields = ['name', 'description', ]
