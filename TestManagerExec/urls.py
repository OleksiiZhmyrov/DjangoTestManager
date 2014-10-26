from django.conf.urls import patterns, url

from TestManagerExec.views import TestCaseResultCreateView, TestStepResultModifyView

urlpatterns = patterns(
    '',

    url(r'^exec/testcases/init/(?P<test_case_pk>[0-9]*)/$', TestCaseResultCreateView.as_view(),
        name='test_case_result_create'),

    url(r'^exec/teststepresults/(?P<pk>[0-9]*)/$', TestStepResultModifyView.as_view(),
        name='test_step_result_modify'),

)


