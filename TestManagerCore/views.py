from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, CreateView

from ManualTester.models import TestSuite
from TestManagerCore.forms import UserRegistrationForm


class UserLogOutView(View):

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/homepage/')


class UserRegistrationView(CreateView):

    template_name = 'pages/register_page.html'
    form_class = UserRegistrationForm
    success_url = '/accounts/login/'


class HomePageView(TemplateView):
    template_name = "pages/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['test_suites'] = TestSuite.objects.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomePageView, self).dispatch(*args, **kwargs)