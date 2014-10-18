from django.contrib import admin
from ManualTester.models import TestCase, TestCaseResult, TestCaseStatus, OrderTestCase
from ManualTester.models import TestStep, TestStepResult, TestStepStatus
from ManualTester.models import ExecutionResult, TestSuite, OrderTestStep

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
