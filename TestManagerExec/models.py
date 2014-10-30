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

    css_styling = models.CharField(
        "Custom CSS styling",
        max_length=128,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Execution Result"
        verbose_name_plural = "Execution Results"


class TestStepResult(models.Model):
    execution_result = models.ForeignKey(
        ExecutionResult,
        related_name="Execution result",
        blank=True,
        null=True,
    )

    tester = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    modification_date = models.DateTimeField(
        "Modification date",
        auto_now=True,
    )

    test_step = models.ForeignKey(TestStep)

    linked_issues = models.ManyToManyField(
        "TestManagerCore.JiraIssue",
        verbose_name="Related Jira Issues",
        blank=True,
        null=True,
    )

    previous_test_step_result = models.ForeignKey(
        "TestManagerExec.TestStepResult",
        related_name='Previous Test Step Result',
        blank=True,
        null=True,
    )

    next_test_step_result = models.ForeignKey(
        "TestManagerExec.TestStepResult",
        related_name='Next Test Step Result',
        blank=True,
        null=True,
    )

    comment = models.CharField(
        "Comment",
        max_length=256,
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

    modification_date = models.DateTimeField(
        "Modification date",
        auto_now=True,
    )

    test_case = models.ForeignKey(TestCase)

    test_step_results = models.ManyToManyField(
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
