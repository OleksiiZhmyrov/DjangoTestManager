from django.db import models
from TestManagerCore.utils import UploadFileHelper


class ApplicationFeature(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    def __str__(self):
        return self.name


class JiraIssue(models.Model):

    key = models.CharField(
        "Key",
        max_length=64
    )

    def __str__(self):
        return self.key


class Tag(models.Model):

    name = models.CharField(
        "Name",
        max_length=64
    )

    def __str__(self):
        return self.name


class Sprint(models.Model):

    name = models.CharField(
        "Name",
        max_length=64
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

    def __str__(self):
        return self.name