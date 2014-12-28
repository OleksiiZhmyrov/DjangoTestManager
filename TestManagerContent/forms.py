from django import forms
from django.template.defaultfilters import filesizeformat
from django_summernote.widgets import SummernoteWidget
from DjangoTestManager.settings import CONTENT_TYPES, MAX_UPLOAD_SIZE

from TestManagerContent.models import TestSuite, TestCase, OrderTestCase, TestCaseStatus, TestStep, OrderTestStep, \
    TestStepStatus
from TestManagerCore.models import Tag, Screenshot, ApplicationFeature, UserProfile
from TestManagerCore.utils import CustomErrorList, BleachWrapper
from TestManagerCore.widgets import GroupedSelect


class TestSuiteBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestSuiteBaseForm, self).__init__(*args, **kwargs)
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


class TestSuiteCreateForm(TestSuiteBaseForm):
    """Form class for creating TestSuite objects."""

    class Meta:
        model = TestSuite
        fields = ['name', 'description', ]


class TestSuiteUpdateForm(TestSuiteBaseForm):
    """Form class for modifying TestSuite objects."""

    def __init__(self, user, *args, **kwargs):
        super(TestSuiteUpdateForm, self).__init__(*args, **kwargs)
        self.project = UserProfile.objects.get(user=user).default_project

        self.fields['tags'] = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.filter(
                project=self.project,
            ),
            widget=forms.CheckboxSelectMultiple(),
            required=False,
        )

    class Meta:
        model = TestSuite
        fields = ['name', 'description', 'tags', ]


class OrderTestCaseBaseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(OrderTestCaseBaseForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.user = user

        self.fields['number'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Integer value',
            },
        )

        self.fields['test_case'].widget = forms.Select(
            choices=((i.pk, i.name) for i in TestCase.objects.filter(
                project=UserProfile.objects.get(user=self.user).default_project,
            )),
            attrs={
                'class': 'form-control',
            },
        )

    class Meta:
        model = OrderTestCase
        fields = ['number', 'test_case', ]


class OrderTestCaseCreateForm(OrderTestCaseBaseForm):
    """Form class for creating OrderTestCase objects."""


class OrderTestCaseModifyForm(OrderTestCaseBaseForm):
    """Form class for creating OrderTestCase objects."""


class TestCaseBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestCaseBaseForm, self).__init__(*args, **kwargs)
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


class TestCaseCreateForm(TestCaseBaseForm):
    """Form class for creating TestCase objects."""

    class Meta:
        model = TestCase
        fields = ['name', 'description', 'status', ]


class TestCaseUpdateForm(TestCaseBaseForm):
    """Form class for updating TestCase objects."""

    def __init__(self, user, *args, **kwargs):
        super(TestCaseUpdateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.project = UserProfile.objects.get(user=user).default_project

        self.fields['tags'] = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.filter(
                project=self.project,
            ),
            widget=forms.CheckboxSelectMultiple(),
            required=False,
        )

    class Meta:
        model = TestCase
        fields = ['name', 'description', 'status', 'tags', ]


class OrderTestStepBaseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(OrderTestStepBaseForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.project = UserProfile.objects.get(user=user).default_project

        self.fields['number'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Integer value',
            },
        )

        self.fields['test_step'].widget = GroupedSelect(
            choices=self._get_test_steps_tuple(),
            attrs={
                'class': 'form-control',
                'size': '20',
            },
        )

    def _get_test_steps_tuple(self):
        result = []
        application_features = ApplicationFeature.objects.filter(
            project=self.project,
        )
        for application_feature in application_features:
            test_steps = (
                (i.pk, i.name) for i in TestStep.objects.filter(
                    application_feature=application_feature,
                    project=self.project,
                )
            )
            result.append((application_feature.name, test_steps))
        return tuple(result)

    class Meta:
        model = OrderTestStep
        fields = ['number', 'test_step', ]


class OrderTestStepCreateForm(OrderTestStepBaseForm):
    """Form class for creating OrderTestStep objects."""


class OrderTestStepModifyForm(OrderTestStepBaseForm):
    """Form class for modifying OrderTestStep objects."""


class TestStepBaseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(TestStepBaseForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.project = UserProfile.objects.get(user=user).default_project

        self.fields['name'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'autofocus': '',
                'required': '',
                'placeholder': 'Name',
            },
        )

        self.fields['description'].widget = SummernoteWidget()

        self.fields['expected_result'].widget = SummernoteWidget()

        self.fields['application_feature'].widget = forms.Select(
            choices=(
                (i.pk, i.name) for i in ApplicationFeature.objects.filter(
                    project=self.project,
                )
            ),
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

    def clean_description(self):
        description = self.cleaned_data['description']
        if description:
            description = BleachWrapper.clean(description)
        return description

    def clean_expected_result(self):
        expected_result = self.cleaned_data['expected_result']
        if expected_result:
            expected_result = BleachWrapper.clean(expected_result)
        return expected_result


class TestStepCreateForm(TestStepBaseForm):
    """Form class to create TestStep objects."""

    class Meta:
        model = TestStep
        fields = ['name', 'description', 'expected_result', 'application_feature', 'status', ]


class TestStepUpdateForm(TestStepBaseForm):
    """Form class to modify TestStep objects."""

    def __init__(self, *args, **kwargs):
        super(TestStepUpdateForm, self).__init__(*args, **kwargs)

        self.fields['screenshot'].widget = GroupedSelect(
            choices=self._get_screenshots_tuple(),
            attrs={
                'class': 'form-control',
                'size': '20',
            },
        )

        self.fields['tags'] = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.filter(
                project=self.project,
            ),
            widget=forms.CheckboxSelectMultiple(),
            required=False,
        )

    def _get_screenshots_tuple(self):
        result = []
        application_features = ApplicationFeature.objects.filter(
            project=self.project,
        )
        for application_feature in application_features:
            screenshots = (
                (i.pk, i.name) for i in Screenshot.objects.filter(
                    application_feature=application_feature,
                    project=self.project,
                )
            )
            result.append((application_feature.name, screenshots))
        return tuple(result)

    class Meta:
        model = TestStep
        fields = ['name', 'description', 'expected_result', 'application_feature', 'status', 'tags', 'screenshot', ]


class ScreenshotBaseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ScreenshotBaseForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList
        self.project = UserProfile.objects.get(user=user).default_project

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

        self.fields['application_feature'].widget = forms.Select(
            choices=(
                (i.pk, i.name) for i in ApplicationFeature.objects.filter(
                    project=self.project,
                )
            ),
            attrs={
                'class': 'form-control',
                'required': '',
            },
        )


class ScreenshotCreateForm(ScreenshotBaseForm):
    """Form class to create Screenshot objects."""

    def clean_screenshot(self):
        screenshot = self.cleaned_data['screenshot']
        if screenshot:
            content_type = screenshot.content_type
            if content_type in CONTENT_TYPES:
                if screenshot.size > MAX_UPLOAD_SIZE:
                    raise forms.ValidationError(
                        'Please keep file size under {max_file_size}. Current file size {current_file_size}'.format(
                            max_file_size=filesizeformat(MAX_UPLOAD_SIZE),
                            current_file_size=filesizeformat(screenshot.size),
                        )
                    )
            else:
                raise forms.ValidationError(
                    'File type is not supported. Supported types are: {types}'.format(
                        types=', '.join(CONTENT_TYPES)
                    )
                )
        return screenshot

    class Meta:
        model = Screenshot
        fields = ['name', 'description', 'application_feature', 'screenshot', ]


class ScreenshotUpdateForm(ScreenshotBaseForm):
    """Form class to modify Screenshot objects."""

    class Meta:
        model = TestStep
        fields = ['name', 'description', 'application_feature', ]
