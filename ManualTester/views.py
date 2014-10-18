from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from ManualTester.forms import TestSuiteCreateForm, TestSuiteUpdateForm
from ManualTester.models import TestSuite


class TestSuiteListView(ListView):
    model = TestSuite
    template_name = "pages/test_suite_list_page.html"

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
    success_url = '/content/testsuites/'

    def get_context_data(self, **kwargs):
        context = super(TestSuiteModifyView, self).get_context_data(**kwargs)
        context['pk'] = self.object.pk
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TestSuiteModifyView, self).dispatch(*args, **kwargs)