from django.contrib import admin
from TestManagerContent.models import TestCase, TestCaseStatus
from TestManagerContent.models import TestStep, TestStepStatus
from TestManagerContent.models import TestSuite

# from TestManagerContent.models import OrderTestCase, OrderTestStep


admin.site.register(TestStep)
admin.site.register(TestCase)
admin.site.register(TestSuite)

# admin.site.register(OrderTestStep)
# admin.site.register(OrderTestCase)

admin.site.register(TestStepStatus)
admin.site.register(TestCaseStatus)

