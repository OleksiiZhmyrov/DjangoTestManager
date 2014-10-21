from django.conf.urls import patterns, url
from ManualTester.views import TestSuiteListView, TestSuiteCreateView, TestSuiteModifyView, OrderTestCaseCreateView, \
    OrderTestCaseDeleteView, OrderTestCaseModifyView, TestSuiteView, TestCaseListView, TestCaseCreateView, \
    TestCaseModifyView


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

    url(r'^content/testcases/modify/(?P<pk>[0-9])/$', TestCaseModifyView.as_view(),
        name='test_case_edit'),

)


