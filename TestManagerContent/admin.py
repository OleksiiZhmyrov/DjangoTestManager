from django.contrib import admin
from TestManagerContent.models import TestCase, TestCaseStatus
from TestManagerContent.models import TestStep, TestStepStatus
from TestManagerContent.models import TestSuite


class TestStepAdmin(admin.ModelAdmin):

    list_display = (
        'author',
        'creation_date',
        'modification_date',
        'name',
        'description',
        'expected_result',
        'screenshot',
        'status',
        'application_feature',
    )

    list_filter = [
        'author',
        'status',
        'application_feature',
    ]

    search_fields = [
        'author',
        'name',
        'description',
        'expected_result',
        'application_feature',
    ]

    date_hierarchy = 'creation_date'

admin.site.register(TestStep, TestStepAdmin)


class TestCaseAdmin(admin.ModelAdmin):

    list_display = (
        'author',
        'creation_date',
        'modification_date',
        'name',
        'description',
        'status',
    )

    list_filter = [
        'author',
        'status',
    ]

    search_fields = [
        'author',
        'name',
        'description',
        'status',
    ]

    date_hierarchy = 'creation_date'

admin.site.register(TestCase, TestCaseAdmin)


class TestSuiteAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'creation_date',
        'modification_date',
        'author',
        'disabled',
    )

    list_filter = [
        'description',
        'author',
        'disabled',
    ]

    search_fields = [
        'name',
        'description',
        'author',
    ]

    date_hierarchy = 'creation_date'

admin.site.register(TestSuite, TestSuiteAdmin)


class TestStepStatusAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'description',
    )

    search_fields = [
        'name',
        'description',
    ]

    date_hierarchy = None

admin.site.register(TestStepStatus, TestStepStatusAdmin)


class TestCaseStatusAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'description',
    )

    search_fields = [
        'name',
        'description',
    ]

    date_hierarchy = None

admin.site.register(TestCaseStatus, TestCaseStatusAdmin)

