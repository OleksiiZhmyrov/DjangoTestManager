from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.forms.util import ErrorList
from django.forms.forms import NON_FIELD_ERRORS
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.views.generic.list import ListView

from ManualTester.forms import TestSuiteCreateForm, TestSuiteUpdateForm, OrderTestCaseCreateForm, \
    OrderTestCaseModifyForm
from ManualTester.models import TestSuite, OrderTestCase


class TestSuiteListView(ListView):
    model = TestSuite
    template_name = "pages/test_suite_list_page.html"
    queryset = TestSuite.objects.filter(disabled=False).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(TestSuiteListView, self).get_context_data(**kwargs)
        context['test_suite_list'] = context['object_list']
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteListView, self).dispatch(*args, **kwargs)


class TestSuiteCreateView(CreateView):
    model = TestSuite
    template_name = "pages/test_suite_create_page.html"
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
    template_name = "pages/test_suite_modify_page.html"
    model = TestSuite
    form_class = TestSuiteUpdateForm

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        """
        Adding pk of the TestSuite object to substitute to form URL.
        """
        context = super(TestSuiteModifyView, self).get_context_data(**kwargs)
        context['pk'] = self.object.pk
        context['order_test_cases'] = OrderTestCase.objects.filter(test_suite=self.object).order_by('number')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteModifyView, self).dispatch(*args, **kwargs)


class OrderTestCaseCreateView(CreateView):
    model = OrderTestCase
    template_name = "pages/ordertestcase_create_page.html"
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
    template_name = "pages/ordertestcase_modify_page.html"
    model = OrderTestCase
    form_class = OrderTestCaseModifyForm

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.test_suite.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestCaseModifyView, self).dispatch(*args, **kwargs)


class OrderTestCaseDeleteView(DeleteView):
    model = OrderTestCase
    template_name = "pages/ordertestcase_remove_page.html"

    def get_success_url(self):
        return reverse('test_suite_edit', args=(self.object.test_suite.id,))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderTestCaseDeleteView, self).dispatch(*args, **kwargs)


class TestSuiteView(DetailView):
    model = TestSuite
    template_name = "pages/test_suite_view_page.html"

    def get_context_data(self, **kwargs):
        context = super(TestSuiteView, self).get_context_data(**kwargs)
        context['test_suite'] = self.object
        context['order_test_cases'] = OrderTestCase.objects.filter(test_suite=self.object).order_by('number')
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteView, self).dispatch(*args, **kwargs)
