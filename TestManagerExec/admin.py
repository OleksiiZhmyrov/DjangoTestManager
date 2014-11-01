from django.contrib import admin
from TestManagerExec.models import TestStepResult, TestCaseResult, ExecutionResult


class TestStepResultAdmin(admin.ModelAdmin):

    list_display = (
        'test_step',
        'execution_result',
        'comment',
        'tester',
        'creation_date',
        'modification_date',
        'previous_test_step_result',
        'next_test_step_result',
    )

    list_filter = [
        'execution_result',
        'tester',
    ]

    search_fields = [
        'test_step',
        'execution_result',
        'comment',
        'tester',
    ]

    date_hierarchy = 'creation_date'

admin.site.register(TestStepResult, TestStepResultAdmin)


class TestCaseResultAdmin(admin.ModelAdmin):

    list_display = (
        'test_case',
        'environment',
        'browser',
        'sprint',
        'tester',
        'creation_date',
        'modification_date',
        'risks',
        'exec_result',
    )

    list_filter = [
        'exec_result',
        'tester',
        'test_case',
        'environment',
        'browser',
        'sprint',
    ]

    search_fields = [
        'exec_result',
        'tester',
        'test_case',
        'environment',
        'browser',
        'sprint',
        'risks',
    ]

    date_hierarchy = 'creation_date'

admin.site.register(TestCaseResult, TestCaseResultAdmin)


class ExecutionResultAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'css_styling',
    )

    search_fields = [
        'name',
        'description',
        'css_styling',
    ]

    date_hierarchy = None

admin.site.register(ExecutionResult, ExecutionResultAdmin)
