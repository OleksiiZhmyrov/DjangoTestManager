from django.forms.utils import ErrorList
from os.path import join
import hashlib

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

        given_filename = '{owner}_{hash}.{ext}'.format(
            owner=instance.author.username,
            hash=m.hexdigest(),
            ext=ext
        )
        return join(path, given_filename)
