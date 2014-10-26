from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView

from DjangoTestManager import settings


urlpatterns = patterns(
    '',
    url(r'', include('TestManagerCore.urls')),
    url(r'', include('TestManagerContent.urls')),
    url(r'', include('TestManagerExec.urls')),

    url(r'^$', RedirectView.as_view(url='/content/testsuites/'), name='redirect_from_root'),

    url(r'^accounts/admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Test Manager admin console'
