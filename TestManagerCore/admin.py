from django.contrib import admin
from TestManagerCore.models import Tag, Sprint, JiraIssue, Browser, Environment, Screenshot, ApplicationFeature
from TestManagerCore.models import UserProfile, Project


class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'default_project',
    )

    list_filter = [
        'default_project',
    ]

    search_fields = [
        'user',
        'default_project',
    ]

    date_hierarchy = None


admin.site.register(UserProfile, UserProfileAdmin)


class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
    )

    search_fields = [
        'name',
        'description',
    ]

    date_hierarchy = None


admin.site.register(Project, ProjectAdmin)


class JiraIssueAdmin(admin.ModelAdmin):

    list_display = (
        'key',
        'project',
        'summary',
    )

    list_filter = [
        'project',
    ]

    search_fields = [
        'key',
        'project',
        'summary',
    ]

    date_hierarchy = None

admin.site.register(JiraIssue, JiraIssueAdmin)


class TagAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'project',
    )

    list_filter = [
        'project',
    ]

    search_fields = [
        'name',
        'project',
    ]

    date_hierarchy = None

admin.site.register(Tag, TagAdmin)


class SprintAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'project',
    )

    list_filter = [
        'project',
    ]

    search_fields = [
        'name',
        'project',
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
        'project',
    )

    list_filter = [
        'project',
    ]

    search_fields = [
        'name',
        'description',
        'url',
        'project',
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
        'project',
    )

    list_filter = [
        'owner',
        'application_feature',
        'project',
    ]

    search_fields = [
        'name',
        'description',
        'application_feature',
        'project',
    ]

    date_hierarchy = 'creation_date'

admin.site.register(Screenshot, ScreenshotAdmin)


class ApplicationFeatureAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'project',
    )

    list_filter = [
        'project',
    ]

    search_fields = [
        'name',
        'project',
    ]

    date_hierarchy = None

admin.site.register(ApplicationFeature, ApplicationFeatureAdmin)
