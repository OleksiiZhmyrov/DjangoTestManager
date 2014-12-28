from django.db import models
from TestManagerCore.utils import UploadFileHelper


class UserProfile(models.Model):

    user = models.ForeignKey(
        "auth.User",

    )

    projects = models.ManyToManyField(
        "TestManagerCore.Project",
        verbose_name="Assigned projects",
        blank=True,
        null=True,
    )

    default_project = models.ForeignKey(
        "TestManagerCore.Project",
        related_name="Default project",
    )

    def __str__(self):
        return self.user.username


class Project(models.Model):

    name = models.CharField(
        "Project name",
        max_length=64,
    )

    description = models.CharField(
        "Description",
        max_length=256,
    )

    def __str__(self):
        return self.name


class ApplicationFeature(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    project = models.ForeignKey(
        "TestManagerCore.Project"
    )

    def __str__(self):
        return self.name


class JiraIssue(models.Model):

    key = models.CharField(
        "Key",
        max_length=64,
    )

    summary = models.CharField(
        "Summary",
        max_length=512,
    )

    project = models.ForeignKey(
        "TestManagerCore.Project"
    )

    def __str__(self):
        return '%s %s' % (self.key, self.summary)


class Tag(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    project = models.ForeignKey(
        "TestManagerCore.Project"
    )

    def __str__(self):
        return self.name


class Sprint(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    project = models.ForeignKey(
        "TestManagerCore.Project"
    )

    def __str__(self):
        return self.name


class Browser(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    version = models.CharField(
        "Version",
        max_length=32,
    )

    note = models.CharField(
        "Note",
        max_length=256,
        blank=True,
        null=True,
    )

    def __str__(self):
        return ' '.join([self.name, self.version])


class Environment(models.Model):

    name = models.CharField(
        "Name",
        max_length=32,
    )

    description = models.CharField(
        "Description",
        max_length=128,
        blank=True,
        null=True,
    )

    url = models.URLField(
        "URL",
        max_length=128,
    )

    project = models.ForeignKey(
        "TestManagerCore.Project"
    )

    def __str__(self):
        return ' '.join([self.name, self.url])


class Screenshot(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    owner = models.ForeignKey("auth.User")

    description = models.CharField(
        "Description",
        max_length=1024,
        blank=True,
        null=True,
    )

    screenshot = models.FileField(
        "Image",
        upload_to=UploadFileHelper.update_filename,
    )

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    application_feature = models.ForeignKey(
        "TestManagerCore.ApplicationFeature"
    )

    project = models.ForeignKey(
        "TestManagerCore.Project"
    )

    def __str__(self):
        return self.name
