from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from TestManagerContent.models import TestCase, OrderTestStep
from TestManagerExec.forms import TestCaseResultCreateForm
from TestManagerExec.models import TestCaseResult, TestStepResult


class TestCaseResultCreateView(CreateView):
    model = TestCaseResult
    template_name = "pages/test_case_result/create_page.html"
    fields = ['environment', 'sprint', 'risks', ]
    form_class = TestCaseResultCreateForm

    def get_context_data(self, **kwargs):
        context = super(TestCaseResultCreateView, self).get_context_data(**kwargs)
        """
            At this moment TestCaseResult object does not have Test Case assigned.
            Therefore test_case template variable contains Test Case for
            displaying on the page.
        """
        context['test_case'] = TestCase.objects.get(
            pk=context['view'].kwargs.get('test_case_pk')
        )
        return context

    def form_valid(self, form):
        form.instance.tester = self.request.user
        form.instance.test_case = TestCase.objects.get(
            pk=self.get_context_data()['view'].kwargs.get('test_case_pk')
        )
        form.save()

        order_test_steps = OrderTestStep.objects.filter(test_case=form.instance.test_case).order_by('number')
        for order_test_step in order_test_steps.all():
            test_step_result = TestStepResult(
                tester=self.request.user,
                test_step=order_test_step.test_step,
            )
            test_step_result.save()
            form.instance.steps_results.add(test_step_result)

        form.save()
        return super(TestCaseResultCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('', args=(self.object.test_case.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestCaseResultCreateView, self).dispatch(*args, **kwargs)