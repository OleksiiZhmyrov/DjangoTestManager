from django.conf.urls import patterns, url

from TestManagerCore.forms import UserLoginForm
from TestManagerCore.views import UserRegistrationView, UserLogOutView, UserProfileUpdateView


urlpatterns = patterns(
    '',
    url(r'^accounts/register/$', UserRegistrationView.as_view(), name='user_registration'),

    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'pages/login_page.html',
            'authentication_form': UserLoginForm
        },
        name='user_login'
    ),

    url(r'^accounts/logout/$', UserLogOutView.as_view(), name='user_logout'),

    url(r'^accounts/profile/$', UserProfileUpdateView.as_view(), name='user_profile'),
)


