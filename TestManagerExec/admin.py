from django.contrib import admin
from TestManagerExec.models import TestStepResult, TestCaseResult, ExecutionResult


admin.site.register(TestStepResult)
admin.site.register(TestCaseResult)
admin.site.register(ExecutionResult)
