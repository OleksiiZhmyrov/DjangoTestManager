from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.urlresolvers import reverse
from django.forms.util import ErrorList
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
import DjangoTestManager
from DjangoTestManager.settings import JIRA_BROWSE_URL
from TestManagerContent.models import TestCase, OrderTestStep
from TestManagerExec.forms import TestCaseResultCreateForm, TestStepResultUpdateForm
from TestManagerExec.models import TestCaseResult, TestStepResult


class TestCaseResultCreateView(CreateView):
    model = TestCaseResult
    template_name = "pages/test_case_result/create_page.html"
    fields = ['environment', 'sprint', 'browser', 'jira_issues', 'risks', ]
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
        """
            Verify if Test Case has included Test Steps and fail form validation
            in case if there are no Test Steps available.
        """
        order_test_steps = OrderTestStep.objects.filter(test_case=form.instance.test_case).order_by('number')
        if not order_test_steps:
            errors = form.errors.setdefault(NON_FIELD_ERRORS, ErrorList())
            errors.append('This Test Case does not have any Test Step and could not be executed.')
            return super(TestCaseResultCreateView, self).form_invalid(form)

        form.save()

        """
            Create TestStepResults objects and link them to current TestCaseResult object.
        """
        for order_test_step in order_test_steps.all():
            test_step_result = TestStepResult(
                tester=self.request.user,
                test_step=order_test_step.test_step,
            )
            test_step_result.save()
            form.instance.test_step_results.add(test_step_result)

        """
            Walk through linked TestStepResult objects and assign previous and next.
        """
        order_test_steps_list = [i for i in form.instance.test_step_results.all()]
        for index, order_test_step in enumerate(order_test_steps_list):
            if index > 0:
                order_test_step.previous_test_step_result = order_test_steps_list[index - 1]
            if index < len(order_test_steps_list) - 1:
                order_test_step.next_test_step_result = order_test_steps_list[index + 1]
            order_test_step.save()

        form.save()
        return super(TestCaseResultCreateView, self).form_valid(form)

    def get_success_url(self):
        """
            Redirect to the first test step execution.
        """
        order_test_step = OrderTestStep.objects.filter(
            test_case=self.object.test_case,
        ).order_by('number')[0]
        test_step_result = self.object.test_step_results.get(
            test_step=order_test_step.test_step
        )
        return reverse('test_step_result_modify', args=(test_step_result.pk,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestCaseResultCreateView, self).dispatch(*args, **kwargs)


class TestStepResultModifyView(UpdateView):
    template_name = "pages/test_step_result/modify_page.html"
    model = TestStepResult
    form_class = TestStepResultUpdateForm
    context_object_name = 'test_step_result'

    def get_context_data(self, **kwargs):
        context = super(TestStepResultModifyView, self).get_context_data(**kwargs)

        test_case_result = TestCaseResult.objects.get(test_step_results=self.object)
        context['test_case_result'] = test_case_result

        test_case = test_case_result.test_case
        context['test_case'] = test_case

        """
            Calculate values for progress bar.
        """
        order_test_steps = OrderTestStep.objects.filter(
            test_case=test_case
        )
        current_order_test_step = order_test_steps.get(
            test_step=self.object.test_step
        )
        current_int = int(current_order_test_step.number)
        total_int = len(order_test_steps)
        context['progress_bar'] = {
            'current': current_int,
            'total': total_int,
            'percentage': 100.0 * current_int / total_int,
        }
        return context

    def get_success_url(self):
        return reverse('test_step_result_modify', args=(self.object.pk,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestStepResultModifyView, self).dispatch(*args, **kwargs)


class TestCaseResultView(DetailView):
    model = TestCaseResult
    template_name = "pages/test_case_result/view_page.html"
    context_object_name = 'test_case_result'

    def get_context_data(self, **kwargs):
        context = super(TestCaseResultView, self).get_context_data(**kwargs)
        context['jira_browse_url'] = JIRA_BROWSE_URL
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestCaseResultView, self).dispatch(*args, **kwargs)