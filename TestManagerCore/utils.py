from django.forms.utils import ErrorList


class CustomErrorList(ErrorList):

    def __str__(self):
        return self.as_help_block()

    def as_help_block(self):
        if not self:
            return ''
        return '<span class="help-block">%s</span>' % ','.join(['%s' % e for e in self])
