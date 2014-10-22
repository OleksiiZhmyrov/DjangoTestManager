from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.forms.util import ErrorList
from django.forms.forms import NON_FIELD_ERRORS
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import ListView

from ManualTester.models import TestSuite, OrderTestCase, TestCase, OrderTestStep

from ManualTester.forms import TestSuiteCreateForm, TestSuiteUpdateForm
from ManualTester.forms import OrderTestCaseCreateForm, OrderTestCaseModifyForm
from ManualTester.forms import TestCaseCreateForm, TestCaseUpdateForm
from ManualTester.forms import OrderTestStepCreateForm, OrderTestStepModifyForm


class TestSuiteListView(ListView):
    model = TestSuite
    template_name = "pages/test_suite/list_page.html"
    queryset = TestSuite.objects.filter(disabled=False).order_by('name')
    context_object_name = 'test_suite_list'
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteListView, self).dispatch(*args, **kwargs)


class TestSuiteCreateView(CreateView):
    model = TestSuite
    template_name = "pages/test_suite/create_page.html"
    fields = ['name', 'description', ]
    form_class = TestSuiteCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(TestSuiteCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteCreateView, self).dispatch(*args, **kwargs)


class TestSuiteModifyView(UpdateView):
    template_name = "pages/test_suite/modify_page.html"
    model = TestSuite
    form_class = TestSuiteUpdateForm
    context_object_name = 'test_suite'

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(TestSuiteModifyView, self).get_context_data(**kwargs)
        context['order_test_cases'] = OrderTestCase.objects.filter(test_suite=self.object).order_by('number')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteModifyView, self).dispatch(*args, **kwargs)


class OrderTestCaseCreateView(CreateView):
    model = OrderTestCase
    template_name = "pages/ordertestcase/create_page.html"
    fields = ['number', 'test_case', ]
    form_class = OrderTestCaseCreateForm

    def get_context_data(self, **kwargs):
        context = super(OrderTestCaseCreateView, self).get_context_data(**kwargs)
        """
            At this moment OrderTestCase object does not have Test Suite assigned.
            Therefore test_suite template variable contains Test Suite for
            displaying on the page.
        """
        context['test_suite'] = TestSuite.objects.get(
            pk=context['view'].kwargs.get('test_suite_pk')
        )
        return context

    def form_valid(self, form):
        form.instance.test_suite = TestSuite.objects.get(
            pk=self.get_context_data()['view'].kwargs.get('test_suite_pk')
        )
        try:
            form.save()
            return super(OrderTestCaseCreateView, self).form_valid(form)
        except IntegrityError:
            """
                Append non-field error to already validated form.
                _errors is a part of Django Forms public API and may be
                accessed from outside of the form class.
                Please refer to documentation for detailed explanation.
            """
            errors = form._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
            errors.append('Test case is already present in Test Suite.')
            return super(OrderTestCaseCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.test_suite.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestCaseCreateView, self).dispatch(*args, **kwargs)


class OrderTestCaseModifyView(UpdateView):
    template_name = "pages/ordertestcase/modify_page.html"
    model = OrderTestCase
    form_class = OrderTestCaseModifyForm

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.test_suite.id,))

    def form_valid(self, form):
        form.instance.test_suite = TestSuite.objects.get(
            pk=self.get_context_data()['view'].kwargs.get('test_suite_pk')
        )
        try:
            form.save()
            return super(OrderTestCaseModifyView, self).form_valid(form)
        except IntegrityError:
            """
                Append non-field error to already validated form.
                _errors is a part of Django Forms public API and may be
                accessed from outside of the form class.
                Please refer to documentation for detailed explanation.
            """
            errors = form._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
            errors.append('Test case is already present in Test Suite.')
            return super(OrderTestCaseModifyView, self).form_invalid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestCaseModifyView, self).dispatch(*args, **kwargs)


class OrderTestCaseDeleteView(DeleteView):
    model = OrderTestCase
    template_name = "pages/ordertestcase/remove_page.html"

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.test_suite.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestCaseDeleteView, self).dispatch(*args, **kwargs)


class TestSuiteView(DetailView):
    model = TestSuite
    template_name = "pages/test_suite/view_page.html"
    context_object_name = 'test_suite'

    def get_context_data(self, **kwargs):
        context = super(TestSuiteView, self).get_context_data(**kwargs)
        context['order_test_cases'] = OrderTestCase.objects.filter(test_suite=self.object).order_by('number')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteView, self).dispatch(*args, **kwargs)


class TestCaseListView(ListView):
    model = TestCase
    template_name = "pages/test_case/list_page.html"
    queryset = TestCase.objects.all().order_by('name')
    context_object_name = 'test_case_list'
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestCaseListView, self).dispatch(*args, **kwargs)


class TestCaseCreateView(CreateView):
    model = TestCase
    template_name = "pages/test_case/create_page.html"
    fields = ['name', 'description', 'status', ]
    form_class = TestCaseCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(TestCaseCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('test_case_edit', args=(self.object.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestCaseCreateView, self).dispatch(*args, **kwargs)


class TestCaseModifyView(UpdateView):
    template_name = "pages/test_case/modify_page.html"
    model = TestCase
    form_class = TestCaseUpdateForm
    context_object_name = 'test_case'

    def get_success_url(self):
        return reverse('test_case_edit', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(TestCaseModifyView, self).get_context_data(**kwargs)
        context['order_test_steps'] = OrderTestStep.objects.filter(test_case=self.object).order_by('number')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestCaseModifyView, self).dispatch(*args, **kwargs)


class TestCaseView(DetailView):
    model = TestCase
    template_name = "pages/test_case/view_page.html"
    context_object_name = 'test_case'

    def get_context_data(self, **kwargs):
        context = super(TestCaseView, self).get_context_data(**kwargs)
        context['order_test_steps'] = OrderTestStep.objects.filter(test_case=self.object).order_by('number')
        context['order_test_cases'] = OrderTestCase.objects.filter(test_case=self.object)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestCaseView, self).dispatch(*args, **kwargs)


class OrderTestStepCreateView(CreateView):
    model = OrderTestStep
    template_name = "pages/orderteststep/create_page.html"
    fields = ['number', 'test_step', ]
    form_class = OrderTestStepCreateForm

    def get_context_data(self, **kwargs):
        context = super(OrderTestStepCreateView, self).get_context_data(**kwargs)
        """
            At this moment OrderTestStep object does not have Test Case assigned.
            Therefore test_case template variable contains Test Case for
            displaying on the page.
        """
        context['test_case'] = TestCase.objects.get(
            pk=context['view'].kwargs.get('test_case_pk')
        )
        return context

    def form_valid(self, form):
        form.instance.test_case = TestCase.objects.get(
            pk=self.get_context_data()['view'].kwargs.get('test_case_pk')
        )
        try:
            form.save()
            return super(OrderTestStepCreateView, self).form_valid(form)
        except IntegrityError:
            """
                Append non-field error to already validated form.
                _errors is a part of Django Forms public API and may be
                accessed from outside of the form class.
                Please refer to documentation for detailed explanation.
            """
            errors = form._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
            errors.append('Test step is already present in Test Case.')
            return super(OrderTestStepCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('test_case_edit', args=(self.object.test_case.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestStepCreateView, self).dispatch(*args, **kwargs)


class OrderTestStepModifyView(UpdateView):
    template_name = "pages/orderteststep/modify_page.html"
    model = OrderTestStep
    form_class = OrderTestStepModifyForm

    def get_success_url(self):
        return reverse('test_case_edit', args=(self.object.test_case.id,))

    def form_valid(self, form):
        form.instance.test_suite = TestCase.objects.get(
            pk=self.get_context_data()['view'].kwargs.get('test_case_pk')
        )
        try:
            form.save()
            return super(OrderTestStepModifyView, self).form_valid(form)
        except IntegrityError:
            """
                Append non-field error to already validated form.
                _errors is a part of Django Forms public API and may be
                accessed from outside of the form class.
                Please refer to documentation for detailed explanation.
            """
            errors = form._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
            errors.append('Test step is already present in Test Case.')
            return super(OrderTestStepModifyView, self).form_invalid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestStepModifyView, self).dispatch(*args, **kwargs)


class OrderTestStepDeleteView(DeleteView):
    model = OrderTestStep
    template_name = "pages/orderteststep/remove_page.html"

    def get_success_url(self):
        return reverse('test_case_edit', args=(self.object.test_case.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestStepDeleteView, self).dispatch(*args, **kwargs)