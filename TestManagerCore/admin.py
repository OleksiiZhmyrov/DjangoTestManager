from django.contrib import admin

from TestManagerCore.models import Tag, Sprint, JiraIssue, Browser, Environment


admin.site.register(JiraIssue)
admin.site.register(Tag)
admin.site.register(Sprint)
admin.site.register(Browser)
admin.site.register(Environment)
