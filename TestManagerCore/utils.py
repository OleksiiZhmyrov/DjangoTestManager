import bleach
from django.forms.utils import ErrorList
from os.path import join
import hashlib
from DjangoTestManager.settings import BLEACH_ALLOWED_TAGS, BLEACH_ALLOWED_ATTRIBUTES, BLEACH_ALLOWED_STYLES
from DjangoTestManager.settings import BLEACH_STRIP_TAGS, BLEACH_STRIP_COMMENTS


class CustomErrorList(ErrorList):

    def __str__(self):
        return self.as_help_block()

    def as_help_block(self):
        if not self:
            return ''
        return '<span class="help-block">%s</span>' % ','.join(['%s' % e for e in self])


class UploadFileHelper(object):

    @staticmethod
    def update_filename(instance, filename):
        path = 'media/uploads/'
        ext = filename.split('.')[-1]
        m = hashlib.md5()
        m.update(filename.encode('utf-8'))

        given_filename = 'img_{hash}.{ext}'.format(
            hash=m.hexdigest(),
            ext=ext
        )
        return join(path, given_filename)


class BleachWrapper(object):
    """
        Wraps clean method of bleach to apply project-wide bleach settings.
    """
    @staticmethod
    def clean(text):
        return bleach.clean(
            text,
            tags=BLEACH_ALLOWED_TAGS,
            attributes=BLEACH_ALLOWED_ATTRIBUTES,
            styles=BLEACH_ALLOWED_STYLES,
            strip=BLEACH_STRIP_TAGS,
            strip_comments=BLEACH_STRIP_COMMENTS,
        )