from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View, CreateView, UpdateView

from TestManagerCore.forms import UserRegistrationForm, UserProfileUpdateForm
from django.core.validators import validate_email


class UserLogOutView(View):

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class UserRegistrationView(CreateView):

    template_name = 'pages/register_page.html'
    form_class = UserRegistrationForm
    success_url = '/accounts/login/'

    def form_valid(self, form):
        form.instance.is_active = False
        try:
            validate_email(form.instance.username)
            form.instance.email = form.instance.username
        except ValidationError:
            pass
        return super(UserRegistrationView, self).form_valid(form)


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
