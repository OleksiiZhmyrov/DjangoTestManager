from django.conf.urls import patterns, url

from TestManagerContent.views import TestSuiteListView
from TestManagerContent.views import TestSuiteView, TestSuiteCreateView, TestSuiteModifyView
from TestManagerContent.views import OrderTestCaseCreateView, OrderTestCaseModifyView, OrderTestCaseDeleteView

from TestManagerContent.views import TestCaseListView
from TestManagerContent.views import TestCaseView, TestCaseCreateView, TestCaseModifyView
from TestManagerContent.views import OrderTestStepCreateView, OrderTestStepModifyView, OrderTestStepDeleteView

from TestManagerContent.views import TestCaseExportAsSpreadsheet

from TestManagerContent.views import TestStepListView
from TestManagerContent.views import TestStepView, TestStepCreateView, TestStepModifyView

from TestManagerContent.views import ScreenshotListView
from TestManagerContent.views import ScreenshotCreateView, ScreenshotModifyView

from TestManagerContent.views import TestCasePrintView


urlpatterns = patterns(
    '',

    url(r'^content/testsuites/$', TestSuiteListView.as_view(),
        name='test_suite_list'),

    url(r'^content/testsuites/create/$', TestSuiteCreateView.as_view(),
        name='test_suite_create'),

    url(r'^content/testsuites/view/(?P<pk>[0-9]*)/$', TestSuiteView.as_view(),
        name='test_suite_view'),

    url(r'^content/testsuites/modify/(?P<pk>[0-9]*)/$', TestSuiteModifyView.as_view(),
        name='test_suite_edit'),

    url(r'^content/testsuites/(?P<test_suite_pk>[0-9]*)/ordertestcase/add/', OrderTestCaseCreateView.as_view(),
        name='ordertestcase_create'),

    url(r'^content/testsuites/(?P<test_suite_pk>[0-9]*)/ordertestcase/(?P<pk>[0-9])/modify/', OrderTestCaseModifyView.as_view(),
        name='ordertestcase_modify'),

    url(r'^content/testsuites/(?P<test_suite_pk>[0-9]*)/ordertestcase/(?P<pk>[0-9])/remove/', OrderTestCaseDeleteView.as_view(),
        name='ordertestcase_remove'),

    url(r'^content/testcases/$', TestCaseListView.as_view(),
        name='test_case_list'),

    url(r'^content/testcases/create/$', TestCaseCreateView.as_view(),
        name='test_case_create'),

    url(r'^content/testcases/view/(?P<pk>[0-9]*)/$', TestCaseView.as_view(),
        name='test_case_view'),

    url(r'^content/testcase/export/spreadsheet/(?P<pk>[0-9]*)', TestCaseExportAsSpreadsheet.as_view(),
        name='test_case_export_as_spreadsheet_view'),

    url(r'^content/testcases/print/(?P<pk>[0-9]*)/$', TestCasePrintView.as_view(),
        name='test_case_print_view'),

    url(r'^content/testcases/modify/(?P<pk>[0-9]*)/$', TestCaseModifyView.as_view(),
        name='test_case_edit'),

    url(r'^content/testcases/(?P<test_case_pk>[0-9]*)/orderteststep/add/', OrderTestStepCreateView.as_view(),
        name='orderteststep_create'),

    url(r'^content/testcases/(?P<test_case_pk>[0-9]*)/orderteststep/(?P<pk>[0-9]*)/modify/', OrderTestStepModifyView.as_view(),
        name='orderteststep_modify'),

    url(r'^content/testcases/(?P<test_case_pk>[0-9]*)/orderteststep/(?P<pk>[0-9]*)/remove/', OrderTestStepDeleteView.as_view(),
        name='orderteststep_remove'),

    url(r'^content/teststeps/$', TestStepListView.as_view(),
        name='test_step_list'),

    url(r'^content/teststeps/view/(?P<pk>[0-9]*)/$', TestStepView.as_view(),
        name='test_step_view'),

    url(r'^content/teststeps/create/$', TestStepCreateView.as_view(),
        name='test_step_create'),

    url(r'^content/teststeps/modify/(?P<pk>[0-9]*)/$', TestStepModifyView.as_view(),
        name='test_step_edit'),

    url(r'^content/screenshots/$', ScreenshotListView.as_view(),
        name='screenshot_list'),

    url(r'^content/screenshots/create/$', ScreenshotCreateView.as_view(),
        name='screenshot_create'),

    url(r'^content/screenshots/modify/(?P<pk>[0-9]*)/$', ScreenshotModifyView.as_view(),
        name='screenshot_edit'),

)


