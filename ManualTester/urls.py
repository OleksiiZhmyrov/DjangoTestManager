from django.conf.urls import patterns, url
from ManualTester.views import TestSuiteListView, TestSuiteCreateView, TestSuiteModifyView


urlpatterns = patterns(
    '',
    url(r'^content/testsuites/$', TestSuiteListView.as_view(), name='test_suite_list'),
    url(r'^content/testsuites/create/$', TestSuiteCreateView.as_view(), name='test_suite_create'),
    url(r'^content/testsuites/modify/(?P<pk>[0-9])/$', TestSuiteModifyView.as_view(), name='test_suite_edit'),

)


