from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, CreateView, UpdateView

from ManualTester.models import TestSuite
from TestManagerCore.forms import UserRegistrationForm, UserProfileUpdateForm


class UserLogOutView(View):

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class UserRegistrationView(CreateView):

    template_name = 'pages/register_page.html'
    form_class = UserRegistrationForm
    success_url = '/accounts/login/'


class UserProfileUpdateView(UpdateView):
    template_name = "pages/profile_page.html"
    model = User
    form_class = UserProfileUpdateForm
    success_url = '/accounts/profile/'

    def get_object(self, queryset=None):
        return self.request.user

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileUpdateView, self).dispatch(*args, **kwargs)
