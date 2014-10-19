from django.conf.urls import patterns, url
from ManualTester.views import TestSuiteListView, TestSuiteCreateView, TestSuiteModifyView, OrderTestCaseCreateView


urlpatterns = patterns(
    '',

    url(r'^content/testsuites/$', TestSuiteListView.as_view(),
        name='test_suite_list'),

    url(r'^content/testsuites/create/$', TestSuiteCreateView.as_view(),
        name='test_suite_create'),

    url(r'^content/testsuites/modify/(?P<pk>[0-9])/$', TestSuiteModifyView.as_view(),
        name='test_suite_edit'),

    url(r'^content/testsuites/(?P<test_suite_pk>[0-9])/ordertestcase/add/', OrderTestCaseCreateView.as_view(),
        name='ordertestcase_create'),

)


