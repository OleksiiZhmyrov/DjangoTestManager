from django.db import models
from TestManagerContent.models import TestStep, TestCase


class ExecutionResult(models.Model):
    name = models.CharField(
        "Name",
        max_length=64,
    )

    description = models.CharField(
        "Description",
        max_length=256,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Execution Result"
        verbose_name_plural = "Execution Results"


class TestStepResult(models.Model):
    exec_result = models.ForeignKey(
        ExecutionResult,
        blank=True,
        null=True,
    )

    tester = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    test_step = models.ForeignKey(TestStep)

    linked_issues = models.ManyToManyField(
        "TestManagerCore.JiraIssue",
        verbose_name="Related Jira Issues",
        blank=True,
        null=True,
    )

    def __str__(self):
        return ', '.join([str(self.pk), self.test_step.name, self.tester.username])

    class Meta:
        verbose_name = "Test Step Result"
        verbose_name_plural = "Test Step Results"


class TestCaseResult(models.Model):
    exec_result = models.ForeignKey(
        ExecutionResult,
        blank=True,
        null=True,
    )

    tester = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    test_case = models.ForeignKey(TestCase)

    steps_results = models.ManyToManyField(
        TestStepResult,
        verbose_name="Results of related test steps",
    )

    environment = models.ForeignKey(
        "TestManagerCore.Environment",
    )

    browser = models.ForeignKey(
        "TestManagerCore.Browser",
        blank=True,
        null=True,
    )

    sprint = models.ForeignKey(
        "TestManagerCore.Sprint",
    )

    risks = models.CharField(
        "Risks",
        max_length=512,
        blank=True,
        null=True,
    )

    def __str__(self):
        return ', '.join([str(self.pk), self.test_case.name, self.environment.name, self.tester.username])

    class Meta:
        verbose_name = "Test Case Result"
        verbose_name_plural = "Test Case Results"
