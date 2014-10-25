from django.contrib import admin
from TestManagerContent.models import TestCase, TestCaseResult, TestCaseStatus, OrderTestCase
from TestManagerContent.models import TestStep, TestStepResult, TestStepStatus
from TestManagerContent.models import ExecutionResult, TestSuite, OrderTestStep

admin.site.register(TestStep)
admin.site.register(TestStepResult)
admin.site.register(TestCase)
admin.site.register(TestCaseResult)
admin.site.register(TestSuite)

# admin.site.register(OrderTestStep)
# admin.site.register(OrderTestCase)

admin.site.register(TestStepStatus)
admin.site.register(TestCaseStatus)
admin.site.register(ExecutionResult)
