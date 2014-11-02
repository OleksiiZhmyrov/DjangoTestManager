from django.contrib import admin

from TestManagerCore.models import Tag, Sprint, JiraIssue, Browser, Environment, Screenshot, ApplicationFeature


class JiraIssueAdmin(admin.ModelAdmin):

    list_display = (
        'key',
        'summary',
    )

    search_fields = [
        'key',
        'summary',
    ]

    date_hierarchy = None

admin.site.register(JiraIssue, JiraIssueAdmin)


class TagAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )

    search_fields = [
        'name',
    ]

    date_hierarchy = None

admin.site.register(Tag, TagAdmin)


class SprintAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )

    search_fields = [
        'name',
    ]

    date_hierarchy = None

admin.site.register(Sprint, SprintAdmin)


class BrowserAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'version',
        'note',
    )

    list_filter = [
        'name'
    ]

    search_fields = [
        'name',
        'version',
        'note',
    ]

    date_hierarchy = None

admin.site.register(Browser, BrowserAdmin)


class EnvironmentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'url',
    )

    search_fields = [
        'name',
        'description',
        'url',
    ]

    date_hierarchy = None

admin.site.register(Environment, EnvironmentAdmin)


class ScreenshotAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'owner',
        'description',
        'screenshot',
        'creation_date',
        'application_feature',
    )

    list_filter = [
        'owner',
        'application_feature',
    ]

    search_fields = [
        'name',
        'description',
        'application_feature',
    ]

    date_hierarchy = 'creation_date'

admin.site.register(Screenshot, ScreenshotAdmin)


class ApplicationFeatureAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
    )

    search_fields = [
        'name',
    ]

    date_hierarchy = None

admin.site.register(ApplicationFeature, ApplicationFeatureAdmin)
