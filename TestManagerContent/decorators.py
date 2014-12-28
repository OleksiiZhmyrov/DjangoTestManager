from TestManagerCore.models import UserProfile
from django.core.exceptions import PermissionDenied
from django.http import Http404


def user_has_access(content_type, pk_field_name='pk'):
    """
        Verify if user has access to the item of content_type
        and raise PermissionDenied if necessary.
    """
    def _decorator(func):
        def _wrap(*args, **kwargs):
            try:
                instance = content_type.objects.get(
                    pk=kwargs.get(pk_field_name),
                )
            except content_type.DoesNotExist:
                raise Http404

            project = UserProfile.objects.get(
                user=args[0].user
            ).default_project

            if hasattr(instance, 'project') and instance.project != project:
                raise PermissionDenied

            if hasattr(instance, 'test_case') and instance.test_case.project != project:
                raise PermissionDenied

            if hasattr(instance, 'test_step') and instance.test_step.project != project:
                raise PermissionDenied

            return func(*args, **kwargs)
        return _wrap
    return _decorator
