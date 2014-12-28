from DjangoTestManager import settings
from time import gmtime, strftime
from TestManagerCore.models import UserProfile


class SessionExpiry(object):
    """ Set the session expiry according to settings """

    def process_request(self, request):
        if getattr(settings, 'SESSION_EXPIRY', None):
            request.session.set_expiry(settings.SESSION_EXPIRY)
        return None


class PageGenerationDatetime(object):
    """Adds a page_generated_datetime variable to response context."""

    def process_template_response(self, request, response):
        dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        response.context_data['page_generated_datetime'] = '%s UTC' % dt
        return response


class UserprofileContextInjector(object):
    """Injects UserProfile object into response context."""

    def process_template_response(self, request, response):
        if request.user.is_authenticated():
            response.context_data['userprofile'] = UserProfile.objects.get(user=request.user)
        return response