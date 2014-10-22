from django.conf.urls import patterns, url

from ManualTester.views import TestSuiteListView
from ManualTester.views import TestSuiteView, TestSuiteCreateView, TestSuiteModifyView
from ManualTester.views import OrderTestCaseCreateView, OrderTestCaseModifyView, OrderTestCaseDeleteView

from ManualTester.views import TestCaseListView
from ManualTester.views import TestCaseView, TestCaseCreateView, TestCaseModifyView
from ManualTester.views import OrderTestStepCreateView, OrderTestStepModifyView, OrderTestStepDeleteView


urlpatterns = patterns(
    '',

    url(r'^content/testsuites/$', TestSuiteListView.as_view(),
        name='test_suite_list'),

    url(r'^content/testsuites/create/$', TestSuiteCreateView.as_view(),
        name='test_suite_create'),

    url(r'^content/testsuites/view/(?P<pk>[0-9])/$', TestSuiteView.as_view(),
        name='test_suite_view'),

    url(r'^content/testsuites/modify/(?P<pk>[0-9])/$', TestSuiteModifyView.as_view(),
        name='test_suite_edit'),

    url(r'^content/testsuites/(?P<test_suite_pk>[0-9])/ordertestcase/add/', OrderTestCaseCreateView.as_view(),
        name='ordertestcase_create'),

    url(r'^content/testsuites/(?P<test_suite_pk>[0-9])/ordertestcase/(?P<pk>[0-9])/modify/', OrderTestCaseModifyView.as_view(),
        name='ordertestcase_modify'),

    url(r'^content/testsuites/(?P<test_suite_pk>[0-9])/ordertestcase/(?P<pk>[0-9])/remove/', OrderTestCaseDeleteView.as_view(),
        name='ordertestcase_remove'),

    url(r'^content/testcases/$', TestCaseListView.as_view(),
        name='test_case_list'),

    url(r'^content/testcases/create/$', TestCaseCreateView.as_view(),
        name='test_case_create'),

    url(r'^content/testcases/view/(?P<pk>[0-9])/$', TestCaseView.as_view(),
        name='test_suite_view'),

    url(r'^content/testcases/modify/(?P<pk>[0-9])/$', TestCaseModifyView.as_view(),
        name='test_case_edit'),

    url(r'^content/testcases/(?P<test_case_pk>[0-9])/orderteststep/add/', OrderTestStepCreateView.as_view(),
        name='orderteststep_create'),

    url(r'^content/testcases/(?P<test_case_pk>[0-9])/orderteststep/(?P<pk>[0-9])/modify/', OrderTestStepModifyView.as_view(),
        name='orderteststep_modify'),

    url(r'^content/testcases/(?P<test_case_pk>[0-9])/orderteststep/(?P<pk>[0-9])/remove/', OrderTestStepDeleteView.as_view(),
        name='orderteststep_remove'),

)


