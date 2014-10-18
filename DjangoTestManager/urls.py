from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from TestManagerCore.forms import UserLoginForm

from TestManagerCore.views import UserRegistrationView, UserLogOutView, UserProfileUpdateView
from TestManagerCore.views import HomePageView
from DjangoTestManager import settings


urlpatterns = patterns(
    '',
    url(r'^homepage/$', HomePageView.as_view(), name='homepage'),

    url(r'', include('ManualTester.urls')),
    url(r'^accounts/admin/', include(admin.site.urls)),

    url(r'^accounts/register/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'pages/login_page.html',
        'authentication_form': UserLoginForm}, name='user_login'),
    url(r'^accounts/logout/$', UserLogOutView.as_view(), name='user_logout'),
    url(r'^accounts/profile/$', UserProfileUpdateView.as_view(), name='user_profile'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Test Manager admin console'
