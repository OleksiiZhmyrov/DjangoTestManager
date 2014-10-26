from django.conf.urls import patterns, url
from TestManagerExec.views import TestCaseResultCreateView

urlpatterns = patterns(
    '',

    url(r'^exec/testcases/run/(?P<test_case_pk>[0-9])/$', TestCaseResultCreateView.as_view(),
        name='test_case_result_create'),

)


