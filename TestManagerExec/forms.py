from django import forms

from TestManagerCore.models import Environment, Sprint, Browser, JiraIssue
from TestManagerCore.utils import CustomErrorList
from TestManagerCore.widgets import GroupedSelectMultiple
from TestManagerExec.models import TestCaseResult, TestStepResult, ExecutionResult


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

        self.fields['browser'].widget = forms.Select(
            choices=self._get_browsers_tupple(),
            attrs={
                'class': 'form-control',
            },
        )

        # self.fields['jira_issues'].widget = forms.SelectMultiple(
        #     choices=((i.pk, '%s: %s' % (i.key, i.summary[:30])) for i in JiraIssue.objects.all()),
        #     attrs={
        #         'class': 'form-control',
        #         'rows': 5,
        #     }
        # )

        self.fields['jira_issues'].widget = GroupedSelectMultiple(
            choices=((False, ((i.pk, '%s: %s' % (i.key, i.summary[:30])) for i in JiraIssue.objects.all())),),
            attrs={
                'class': 'form-control',
                'size': '6',
                'multiple': '',
            },
        )

        self.fields['risks'].widget = forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Assumptions and risks',
            },
        )

    @staticmethod
    def _get_browsers_tupple():
        browser_queryset = Browser.objects.all().order_by('name', '-version')
        browsers = [('', 'none')] + [(i.pk, ' '.join([i.name, i.version])) for i in browser_queryset]
        return list(browsers)

    class Meta:
        model = TestCaseResult
        fields = ['environment', 'sprint', 'browser', 'jira_issues', 'risks', ]


class TestStepResultUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestStepResultUpdateForm, self).__init__(*args, **kwargs)
        self.error_class = CustomErrorList

        self.fields['execution_result'].widget = forms.Select(
            choices=((i.pk, i.name) for i in ExecutionResult.objects.all()),
            attrs={
                'class': 'form-control',
                'required': '',
            },
        )

        self.fields['comment'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Comments',
            },
        )

    class Meta:
        model = TestStepResult
        fields = ['execution_result', 'comment', ]

